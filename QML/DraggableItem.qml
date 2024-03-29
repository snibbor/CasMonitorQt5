import QtQuick 2.15
import QtQml.Models 2.15
import Qt.labs.qmlmodels 1.0
import QtQuick.Controls 2.15
import "./Icons/"


Item {
    id: root

    default property Item contentItem

    // This item will become the parent of the dragged item during the drag operation
    property Item draggedItemParent

    signal moveItemRequested(int from, int to)

    // Size of the area at the top and bottom of the list where drag-scrolling happens
    property int scrollEdgeSize: 6

    // Internal: set to -1 when drag-scrolling up and 1 when drag-scrolling down
    property int _scrollingDirection: 0

    // Internal: shortcut to access the attached ListView from everywhere. Shorter than root.ListView.view
    property ListView _listView: ListView.view
    property DelegateModel modDel: DelegateModel.model

    property int dHeight: contentItem.height

    width: contentItem.width
    height: topPlaceholder.height + wrapperParent.height + bottomPlaceholder.height

    // Make contentItem a child of contentItemWrapper
    onContentItemChanged: {
        contentItem.parent = contentItemWrapper;
    }

    Rectangle {
        id: topPlaceholder
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
        }
        height: 0
        color: "lightgrey"
    }

    Item {
        id: wrapperParent
        anchors {
            left: parent.left
            right: parent.right
            top: topPlaceholder.bottom
        }
        height: contentItem.height

        Rectangle {
            id: contentItemWrapper
            anchors.fill: parent
            Drag.active: dragArea.drag.active
            Drag.source: contentItem
            Drag.hotSpot {
                x: contentItem.width / 2
                y: contentItem.height / 2
            }
            Drag.keys: ["step"]


            MouseArea {
                id: dragArea
                anchors.fill: parent
                drag.target: parent
                // Disable smoothed so that the Item pixel from where we started the drag remains under the mouse cursor
                drag.smoothed: false

                onReleased: {
                    if (drag.active) {
                        emitMoveItemRequested();
                    }

                }

            }
        }
    }

    Rectangle {
        id: bottomPlaceholder
        anchors {
            left: parent.left
            right: parent.right
            top: wrapperParent.bottom
        }
        height: 0
        color: "lightgrey"
    }

    SmoothedAnimation {
        id: upAnimation
        target: _listView
        property: "contentY"
        to: 0
        running: _scrollingDirection == -1
    }

    SmoothedAnimation {
        id: downAnimation
        target: _listView
        property: "contentY"
        to: _listView.contentHeight - _listView.height
        running: _scrollingDirection == 1
    }

    Loader {
        id: topDropAreaLoader
        active: model.index === 0
        anchors {
            left: parent.left
            right: parent.right
            bottom: wrapperParent.verticalCenter
        }
        height: contentItem.height
        sourceComponent: Component {
            DropArea {
                id:topDropArea
                property int dropIndex: 0
                keys: ["step", "operation"]

                onDropped: {
//                    console.log("Dropped top!")
//                    console.log("dropI: ", dropIndex)
//                    console.log("modelI: ", model.index)
                    if(drag.source.type == "operation"){
                        modDel.model.insert(dropIndex, _listView.operDict[drag.source.opName]);
                        console.log(JSON.stringify(_listView.operDict[drag.source.opName]))
                    }
                }

                onEntered: {
                    if('minimize' in drag.source){drag.source.minimize = true}
                    root.dHeight = drag.source.height
                }
            }
        }
    }

    DropArea {
        id: bottomDropArea
        keys: ["step", "operation"]
        anchors {
            left: parent.left
            right: parent.right
            top: wrapperParent.verticalCenter
        }
        property bool isLast: model.index === _listView.count - 1
        height: isLast ? _listView.contentHeight - bottomDropArea.y : contentItem.height

        property int dropIndex: model.index + 1


        onDropped: {
//            console.log("Dropped bottom!")
//            console.log("modelI: ", model.index)
            if(drag.source.type == "operation"){
                modDel.model.insert(dropIndex, _listView.operDict[drag.source.opName]);
                console.log(JSON.stringify(_listView.operDict[drag.source.opName]))
            }
        }

        onEntered: {
            if('minimize' in drag.source){drag.source.minimize = true}
            root.dHeight = drag.source.height
        }

    }

    states: [
        State {
            when: dragArea.drag.active
            name: "dragging"

            ParentChange {
                target: contentItemWrapper
                parent: draggedItemParent
            }
            PropertyChanges {
                target: contentItemWrapper
                opacity: 0.9
                anchors.fill: undefined
                width: contentItem.width
                height: contentItem.height
            }
            PropertyChanges {
                target: wrapperParent
                height: 0
            }
            PropertyChanges {
                target: root
                _scrollingDirection: {
                    var yCoord = _listView.mapFromItem(dragArea, 0, dragArea.mouseY).y;
                    if (yCoord < scrollEdgeSize) {
                        -1;
                    } else if (yCoord > _listView.height - scrollEdgeSize) {
                        1;
                    } else {
                        0;
                    }
                }
            }
        },
        State {
            when: bottomDropArea.containsDrag
            name: "droppingBelow"
            PropertyChanges {
                target: bottomPlaceholder
                height: root.dHeight
            }
            PropertyChanges {
                target: bottomDropArea
                height: 2*root.dHeight
            }
        },
        State {
            when: model.index === 0 && topDropAreaLoader.item.containsDrag
            name: "droppingAbove"
            PropertyChanges {
                target: topPlaceholder
                height: root.dHeight
            }
            PropertyChanges {
                target: topDropAreaLoader
                height: 2*root.dHeight
            }
        }
    ]

    function emitMoveItemRequested() {
        var dropArea = contentItemWrapper.Drag.target;
        if (!dropArea) {
            return;
        }
        var dropIndex = dropArea.dropIndex;

        // If the target item is below us, then decrement dropIndex because the target item is going to move up when
        // our item leaves its place
        if (model.index < dropIndex) {
            dropIndex--;
        }
        if (model.index === dropIndex) {
            return;
        }
        root.moveItemRequested(model.index, dropIndex);

        // Scroll the ListView to ensure the dropped item is visible. This is required when dropping an item after the
        // last item of the view. Delay the scroll using a Timer because we have to wait until the view has moved the
        // item before we can scroll to it.
        makeDroppedItemVisibleTimer.start();
    }

    Timer {
        id: makeDroppedItemVisibleTimer
        interval: 0
        onTriggered: {
            _listView.positionViewAtIndex(model.index, ListView.Contain);
        }
    }
}
