# -*- coding: utf-8 -*-

"""
***************************************************************************
    SextanteUtils.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
import time
import sys

class SextanteUtils:

    NUM_EXPORTED = 1

    @staticmethod
    def userFolder():
        userfolder = os.path.expanduser("~") + os.sep + "sextante"
        mkdir(userfolder)

        return userfolder

    @staticmethod
    def isWindows():
        return os.name =="nt"

    @staticmethod
    def isMac():
        return sys.platform == "darwin"

    @staticmethod
    def tempFolder():
        tempfolder = os.path.expanduser("~") + os.sep + "sextante" + os.sep + "tempdata"
        mkdir(tempfolder)

        return tempfolder

    @staticmethod
    def setTempOutput(out, alg):
        ext = out.getDefaultFileExtension(alg)
        validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        safeCmdName = ''.join(c for c in alg.commandLineName() if c in validChars)
        filename = SextanteUtils.tempFolder() + os.sep + safeCmdName + str(SextanteUtils.NUM_EXPORTED) + "." + ext
        out.value = filename
        SextanteUtils.NUM_EXPORTED += 1

    @staticmethod
    def getTempFilename(ext):
        path = SextanteUtils.tempFolder()
        filename = path + os.sep + str(time.time()) + str(SextanteUtils.getNumExportedLayers()) + "." + ext
        return filename

    @staticmethod
    def getNumExportedLayers():
        SextanteUtils.NUM_EXPORTED += 1
        return SextanteUtils.NUM_EXPORTED

def mkdir(newdir):
    if os.path.isdir(newdir):
        pass
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            mkdir(head)
        if tail:
            os.mkdir(newdir)


