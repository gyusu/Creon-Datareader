# coding=utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            # column마다 type 다를 경우 여기를 수정
            if role == QtCore.Qt.DisplayRole:
                if (index.column() == 0):
                    return str(self._data.values[index.row()][index.column()])
                else:
                    return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[section]
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return str(self._data.index[section])
        return None

    def flags(self, index):
        flags = super(self.__class__, self).flags(index)
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEnabled
        return flags


# usage
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    df = pd.DataFrame()
    df['Field1'] = np.arange(0, 10, .5)
    df['Field2'] = np.arange(0, 10, .5)
    app = QtWidgets.QApplication([])
    table = QtWidgets.QTableView()
    mymodel = PandasModel(df)
    table.setSelectionMode(QtWidgets.QTableView.MultiSelection)
    table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

    table.setModel(mymodel)

    table.show()
    app.exec_()
