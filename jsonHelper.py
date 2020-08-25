#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:24:35 2020

@author: jackr
"""

from PyQt5 import QtCore
import json
import jsonschema
# from jsonschema import validate

class JSONHelper(QtCore.QObject):
    # Can be redone with getters and setters for the stepModel property. This will be faster with less conversions on the data object.
    # https://qmlbook.github.io/ch18-python/python.html
    
    nextModel = QtCore.pyqtSignal(str, str, str)
    
    @QtCore.pyqtSlot(str, str)
    def saveProtocol(self, fileName, jString):
        # with open(fileName, "w") as outfile: 
        #     json.dump(jString, outfile) 
        with open(fileName, "w") as outfile: 
            outfile.write(jString) 
    
    @QtCore.pyqtSlot(str, str, str)
    def openProtocol(self, fileName, protocolName, pathSaved):
        # take accepted filename and check if it's .json
        jsondata=[]
        try:
            with open(fileName, encoding='utf-8') as data_file:
                jsondata = json.load(data_file)
        except:
            print("An error has occurred with the file selected.")
            return
            
        # validate .json object?
        # check if json object has the propper keys for all elements?
        isValid = self.validateJson(jsondata)
        if not isValid:
            print('JSON has key value error. opName, opTime, volume, pSpeed, numCycles, and loadType are the only keys accepted.')
            return
        else:
            # Send JSON string with file info
            self.nextModel.emit(json.dumps(jsondata), protocolName, pathSaved)
            
            
    def openToRun(self, fileName):
        # take accepted filename and check if it's .json
        jsondata=[]
        try:
            with open(fileName, encoding='utf-8') as data_file:
                jsondata = json.load(data_file)
        except:
            print("An error has occurred with the file selected.")
            return
            
        # validate .json object?
        # check if json object has the propper keys for all elements?
        isValid = self.validateJson(jsondata)
        if not isValid:
            print('JSON has key value error. opName, opTime, volume, pSpeed, numCycles, and loadType are the only keys accepted.')
            return
        else:
            # Send JSON string with file info
            return(jsondata)
            
    
    def validateJson(self, jsonData):
        # Describe what kind of json you expect.
        # Need to make this more functional with filter masks or regex
        protocolSchema = {
            "type": "array",
            "properties": {
                "opName": {"type": "string"},
                "opTime": {"type": "string"},
                "volume": {"type": "string"},
                "pSpeed": {"type": "string"},
                "numCycles": {"type": "string"},
                "loadType": {"type": "string"},
            },
        }
        try:
            jsonschema.validate(instance=jsonData, schema=protocolSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True