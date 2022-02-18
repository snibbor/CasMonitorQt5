import logging
from serial import Serial
from colorlog import ColoredFormatter
import time
import os

formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

PUMP_Z_PER_ML = 30

PORTS = {
    'PUMP': '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0',
    'CAS1': '/dev/serial/by-id/usb-Adafruit_Feather_M0_553A42195050413837202020FF0D0E3E-if00',
    'CAS2': '/dev/serial/by-id/usb-Adafruit_Feather_M0_49405C675050413837202020FF0D1512-if00',
    'CAS3': '/dev/serial/by-id/usb-Adafruit_Feather_M0_04FC93675050413837202020FF0D0B12-if00',
    'MUX': '/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A9KXBQ1L-if00-port0',
}

s = {}

WASTE = 5
BABB = 8
DYE = 1
AIR = 4
FORMALIN = 7
MEOH = 6
CAS1 = 2
CAS2 = 10
CAS3 = 9

def connect():
    global s

    logger.info('connect to pump')
    s['PUMP'] = Serial(PORTS['PUMP'], baudrate=115200, timeout=0.5)
    time.sleep(3)
    s['PUMP'].readall()

    logger.info('connect to mux')
    #rotating valve
    s['MUX'] = Serial(PORTS['MUX'], baudrate=9600, timeout=0.1)
    s['MUX'].readall()

    logger.info('connect to casettes')
    #motors that engage cassettes
    s['CAS1'] = Serial(PORTS['CAS1'], baudrate=115200, timeout=0.1)
    s['CAS2'] = Serial(PORTS['CAS2'], baudrate=115200, timeout=0.1)
    s['CAS3'] = Serial(PORTS['CAS3'], baudrate=115200, timeout=0.1)

#Only do one time at begining, when the app is open
def acquire():
    logger.info('trying to acquire hardware control')

    if os.path.isfile('/run/shm/prepbot.lock'):
        logger.info('hardware locked, waiting')

    while True:
        try:
            open('/run/shm/prepbot.lock', 'x')
            break
        except FileExistsError:
            continue

    logger.info('got hardware')

    connect()
    if not pump_is_homed():
        pump_home()

#When shut down controller
def release():
    logger.info('releasing hardware control')
    for p in s.values():
        p.close()
    os.remove('/run/shm/prepbot.lock')

def pump_home():
    logger.info('homing pump')
    wait_move_done()

    mux_to(WASTE)

    send('PUMP', 'g01 z150 f2000')
    wait_move_done()
    send('PUMP', 'g92 z0')
    send('PUMP', 'g01 z-2 f500')
    wait_move_done()
    send('PUMP', 'g92 z0')

    open('/run/shm/pump_homed', 'w')

def pump_is_homed():
    return os.path.isfile('/run/shm/pump_homed')

def pump_to(z, speed=200):
    send('PUMP', 'g01 z{} f{}'.format(z, speed))

def pump_to_ml(ml, speed=200):
    pump_to(ml * PUMP_Z_PER_ML, speed)

def send(d, m, read_response=False):
    logger.debug('send message to {}: {}'.format(d, m))
    s[d].write((m+'\n').encode())
    if read_response:
        return s[d].readall().decode()

def wait_ok(msg='ok'):
    logger.debug('waiting for message: {}'.format(msg))
    while True:
        m = s['PUMP'].readall().decode()
        if m:
            logger.debug(m)
        if msg in m:
            logger.debug('message received')
            return

def wait_move_done():
    logger.debug('waiting for move to complete')
    _ = s['PUMP'].readall()
    send('PUMP', 'g4 p0', read_response=False)
    wait_ok()

def mux_to(p):
    logger.debug('MUX TO {}'.format(p))
    s['MUX'].write('GO{}\n'.format(p).encode())
    time.sleep(0.5)

def set_heater(c, T):
    logger.info('Setting heater {} to {}C'.format(c, T))
    s[c].write('T{}'.format(T).encode())

def cassette_eject(c):
    logger.debug('Ejecting cassette {}'.format(c))
    if not cassette_inserted(c):
        logger.warn('NO CASSETTE INSERTED, NOT MOVING')
        return
    s[c].write(b'E')

def cassette_contact(c):
    logger.debug('Move cassette {} to contact heater'.format(c))
    if not cassette_inserted(c):
        logger.warn('NO CASSETTE INSERTED, NOT MOVING')
        return
    s[c].write(b'C')

def cassette_inserted(c):
    s[c].flushInput()
    while True:
        l = s[c].readline().decode()
        if not l.startswith('SW: '):
            continue
        return l[8] == '1'

def cassette_temp(c):
    s[c].flushInput()
    while True:
        l = s[c].readline().decode()
        if not l.startswith('C = '):
            continue
        return float(l[4:])

