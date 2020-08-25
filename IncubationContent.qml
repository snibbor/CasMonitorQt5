import QtQuick 2.12
import QtQml.Models 2.12
import Qt.labs.qmlmodels 1.0
import QtQuick.Controls 2.12
import "./Icons/"



Item {
    id: rootCol

//    property string opName: model.opName
//    property string opTime: model.opTime
    property DelegateModel modDel: null
    property int itemIndex : DelegateModel.itemsIndex
    property bool minimize: true

    property string type: "step"


    width: parent.width
    height: ribbon.height + container.height

    Rectangle {
        id: ribbon
        anchors.top: rootCol.top
        anchors.topMargin: 0

        radius: 5
        width: rootCol.width
        height: 35
        gradient: Gradient {
            orientation: Gradient.Horizontal
            GradientStop {position: 0.524; color: "#f5f5f5"}
            GradientStop {position: 0.826; color: rootCol.minimize ?  "#577dc7" : "#ffc700"}
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
            icon.color: closeButton.down || closeButton.checked || closeButton.highlighted ? "red" : "black"
            icon.width: 30
            icon.height: 30

            onClicked: {
                modDel.items.remove(itemIndex)
                modDel.model.remove(itemIndex)
            }


            background: Rectangle {
                implicitWidth: 30
                implicitHeight: 30
                color: "transparent"
            }

        }

        Text {
            id: opTimeText
            property string opHour: opTime.substring(0,2)
            property string opMin: opTime.substring(3,5)
            property string opSec: opTime.substring(6,8)
            y: 7
            color: "#000000"
            text: opTime
//                text: "12:59:59"
            anchors.verticalCenter: toolButton.verticalCenter
            anchors.left: toolButton.right
            anchors.leftMargin: 10

            font.capitalization: Font.MixedCase
            font.weight: Font.Medium
            font.pointSize: 12
            renderType: Text.QtRendering
        }

        ToolButton {
            id: toolButton
            width: 180
            text: (itemIndex+1) + ". Incubation"
//            text: "99. Incubation"
            opacity: 1
            leftPadding: 6
            rightPadding: 43
            topPadding: 6
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            display: AbstractButton.TextBesideIcon

            contentItem: Item {
                id: element
//                Row {
//                    id: row
//                    anchors.verticalCenter: parent.verticalCenter
//                    layoutDirection: Qt.LeftToRight
////                    anchors.horizontalCenter: parent.horizontalCenter
//                    spacing: 5
                    Image {
                        source: rootCol.minimize ? "Icons/rightArrow-black.png" : "Icons/downArrow-black.png"
                        width: 8
                        height: 8
                        anchors.left: parent.left
                        anchors.leftMargin: 2
                        anchors.verticalCenter: parent.verticalCenter
                    }
                    Text {
                        text: toolButton.text
                        anchors.left: parent.left
                        anchors.leftMargin: 18
                        anchors.verticalCenter: parent.verticalCenter
                        font.weight: Font.Thin
                        font.bold: true
                        font.pointSize: 13
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                    }
//                }
            }

            background: Rectangle {
                    opacity: toolButton.down ? 1.0 : 0.5
                    color: toolButton.down || toolButton.checked || toolButton.highlighted ? toolButton.palette.mid : toolButton.palette.button
                }


            onClicked: {
                rootCol.minimize = rootCol.minimize ? false : true
            }
        }
    }
    Rectangle {
        id: container
        anchors.top: ribbon.bottom

        width: rootCol.width
        height: rootCol.minimize ? 0 : 150

        radius: 5
        border.width: 0.5
        border.color: "lightgray"
        color: "#f5f5f5"
        visible: rootCol.minimize ? false : true

        Text {
            id: runTimeLabel
            color: "#000000"
            text: "Run Time:"
            anchors.verticalCenterOffset: -14
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 25
            font.pointSize: 12
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
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
                } else {
                    opTimeText.opHour = hoursTumbler.currentIndex
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
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
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
                } else {
                    opTimeText.opMin = minutesTumbler.currentIndex
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
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
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
                } else {
                    opTimeText.opSec = secondsTumbler.currentIndex
                    opTime = opTimeText.opHour+":"+opTimeText.opMin+":"+opTimeText.opSec
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



