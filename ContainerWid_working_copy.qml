import QtQuick 2.14
import QtQml.Models 2.14
import Qt.labs.qmlmodels 1.0
import QtQuick.Controls 2.14
import "./Icons/"

MouseArea {
    id: dragArea
    property string runTime: "00:00:00"
    property DelegateModel modDel: null
    property ListView _listView: ListView.view
    property int itemIndex : DelegateModel.itemsIndex
    property int marginVert : 5

    property string type: "step"

    property bool held: false

    anchors {
        left: parent.left; right: parent.right
    }

    width: {
        console.log("model ", model.index)
//        console.log(modDel.model.index)
        console.log(itemIndex)
        return 550
    }

    height: rootCol.height

    drag.target: held ? rootCol : undefined
    drag.axis: Drag.YAxis

    pressAndHoldInterval: 50

    onPressAndHold: held = true
    onReleased: held = false


    Item {
        id: rootCol
        width: dragArea.width
        height: ribbon.height + container.height
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        states: [
            State {
                when: dragArea.held

                ParentChange { target: rootCol; parent: _listView }
                AnchorChanges {
                    target: rootCol
                    anchors { horizontalCenter: undefined; verticalCenter: undefined }
                }
            }
        ]

        Drag.active: dragArea.held
        Drag.source: dragArea
        Drag.hotSpot.x: rootCol.width / 2
        Drag.hotSpot.y: rootCol.height / 2
        Drag.keys: ["step"]


        Rectangle {
            id: ribbon
            anchors.top: rootCol.top
            anchors.topMargin: 0

            radius: 5
            width: rootCol.width
            height: 30
            gradient: Gradient {
                orientation: Gradient.Horizontal
                GradientStop {position: 0.524; color: "#f5f5f5"}
                GradientStop {position: 0.826; color: toolButton.tCheck ? "#ffc700" : "#577dc7"}
            }

            Button {
                id: closeButton
                x: 544
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                anchors.rightMargin: 10
                icon.name: "close-X"
                icon.source: "Icons/close.png"
                icon.color: "black"
                icon.width: 30
                icon.height: 30

                onClicked: {
                    modDel.items.remove(itemIndex)
                    modDel.model.remove(itemIndex)
                }

                background: Rectangle {
                    implicitWidth: 30
                    implicitHeight: 30
                    border.width: closeButton.activeFocus ? 2 : 1
                    border.color: closeButton.down || closeButton.checked || closeButton.highlighted ? "black" : "transparent"
                    radius: 18
                    opacity: closeButton.down ? 0.75 : 1
                    color: closeButton.down || closeButton.checked || closeButton.highlighted ? "red" : "transparent"
                }

            }

            Text {
                id: opTimeText
                property string opHour: opTime.substring(0,2)
                property string opMin: opTime.substring(3,5)
                property string opSec: opTime.substring(6,8)
                y: 7
                color: "#000000"
                text: {return opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec}
//                text: "12:59:59"
                anchors.verticalCenter: toolButton.verticalCenter
                anchors.left: toolButton.right
                anchors.leftMargin: 35

                font.capitalization: Font.MixedCase
                font.weight: Font.Medium
                font.pointSize: 14
                renderType: Text.QtRendering
            }

            ToolButton {
                id: toolButton
                property bool tCheck: false
                width: 130
                text: qsTr("Incubation")
                opacity: 1
                leftPadding: 6
                topPadding: 6
                font.weight: Font.Thin
                font.bold: true
                font.pointSize: 14
                anchors.top: parent.top
                anchors.topMargin: 0
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.left: parent.left
                anchors.leftMargin: 0
                display: AbstractButton.TextBesideIcon

                icon.name: "arrow"
                icon.source: toolButton.tCheck ? "Icons/downArrow-black.png" : "Icons/rightArrow-black.png"
                icon.width: 8
                icon.height: 8

                onClicked: {
                    container.height = container.height ? 0 : 100
                    container.visible = container.visible ? false : true
//                    dragArea.height = dragArea.height ? ribbon.height + container.height : ribbon.height
                    toolButton.tCheck = toolButton.tCheck ? false : true
//                    console.log("dragAreaH: ", dragArea.height, " and rootColH: ", rootCol.height)
                }
            }
        }
        Rectangle {
            id: container
            anchors.top: ribbon.bottom

            width: rootCol.width
            height: 0

            radius: 5
            border.width: 0.5
            border.color: "lightgray"
            color: "#f5f5f5"
            visible: false

            Text {
                id: runTimeLabel
                color: "#000000"
                text: "Run Time:"
                anchors.verticalCenterOffset: -14
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 53
                font.pointSize: 14
                font.weight: Font.Medium
                renderType: Text.QtRendering
                font.capitalization: Font.MixedCase
            }

            Tumbler {
                id: hoursTumbler
                width: 70
                anchors.left: runTimeLabel.right
                anchors.leftMargin: 18
                font.pointSize: 14
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 8
                anchors.top: parent.top
                anchors.topMargin: 10
                transformOrigin: Item.Center
                model: 12

                currentIndex: getHour(opTime)



                onMovingChanged: {
                    if(hoursTumbler.currentIndex < 10){
                    opTimeText.opHour = "0"+hoursTumbler.currentIndex
                    } else {
                    opTimeText.opHour = hoursTumbler.currentIndex
                    }
                    console.log("Hours: ", hoursTumbler.currentIndex)
                }

            }

            Tumbler {
                id: minutesTumbler
                width: 70
                anchors.left: hoursTumbler.right
                anchors.leftMargin: 0
                font.pointSize: 14
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 8
                anchors.top: parent.top
                anchors.topMargin: 10
                transformOrigin: Item.Center
                scale: 1
                rotation: 0
                model: 60

                currentIndex: getMin(opTime)

                onMovingChanged: {
                    if(minutesTumbler.currentIndex < 10){
                    opTimeText.opMin = "0"+minutesTumbler.currentIndex
                    } else {
                    opTimeText.opMin = minutesTumbler.currentIndex
                    }
                    console.log("Minutes: ", minutesTumbler.currentIndex)
                }
            }

            Tumbler {
                id: secondsTumbler
                width: 70
                anchors.left: minutesTumbler.right
                anchors.leftMargin: 0
                font.pointSize: 14
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 8
                anchors.top: parent.top
                anchors.topMargin: 10
                transformOrigin: Item.Center
                model: 60

                currentIndex: getSec(opTime)

                onMovingChanged: {
                    if(secondsTumbler.currentIndex < 10){
                        opTimeText.opSec = "0"+secondsTumbler.currentIndex
                    } else {
                        opTimeText.opSec = secondsTumbler.currentIndex
                    }
                    console.log("Secs: ", secondsTumbler.currentIndex)
                }
            }

            Text {
                id: runTimeLabel1
                x: 9
                color: "#000000"
                text: "(hh:mm:ss)"
                anchors.horizontalCenter: runTimeLabel.horizontalCenter
                anchors.top: runTimeLabel.bottom
                anchors.topMargin: 2
                font.pointSize: 11
                font.weight: Font.Medium
                renderType: Text.QtRendering
                font.capitalization: Font.MixedCase
            }



        }

    }

    DropArea {
        id: dropArea
        anchors.fill: parent
        keys: ["step", "operation"]

        anchors.bottomMargin: {
//            console.log("Anchor running")
            var botMargin = _listView.height - _listView.contentHeight
            if(modDel.items.count !==0 && dragArea.itemIndex==modDel.items.count-1){
                return -1*botMargin
            } else{
                return -1*marginVert
            }
        }

        onEntered: {
            if(modDel !== null && drag.source.type == "step"){
//                modDel.items.move(drag.source.itemIndex, dragArea.itemIndex,1)
                modDel.model.move(drag.source.itemIndex, dragArea.itemIndex,1)
                console.log("Held: ", drag.source.itemIndex)
                console.log("OnTopOf: ", dragArea.itemIndex)
            } else if(modDel !== null && drag.source.type == "operation"){
                //Insert a placeholder item when an operation is ontop of the drop area of a dragDelegate
                //How do you insert a placeholder when an operation is inbetween delegates?
                var below = modDel.items.count - dragArea.itemIndex - 1
//                modDel.items.move(dragArea.itemIndex, dragArea.itemIndex+1, below)
                //                console.log("Below: ", below)
                //                console.log("dAIndex: ", dragArea.itemIndex)
            }
        }



    }

    function getHour(opTime){
        var hour = opTime.substring(0,2)
        if(parseInt(hour.substring(0,1)) == 0){
            return parseInt(hour.substring(1,2))
        } else {
            return parseInt(hour)
        }
    }

    function getMin(opTime){
        var mn = opTime.substring(3,5)
        if(parseInt(mn.substring(0,1)) == 0){
            return parseInt(mn.substring(1,2))
        } else {
            return parseInt(mn)
        }
    }

    function getSec(opTime){
        var sec = opTime.substring(6,8)
        if(parseInt(sec.substring(0,1)) == 0){
            return parseInt(sec.substring(1,2))
        } else {
            return parseInt(sec)
        }
    }
}
