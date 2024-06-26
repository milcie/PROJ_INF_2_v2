# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PROJ_INF_2_v2
                                 A QGIS plugin
 nasza pierwsza wtyczka
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-03
        copyright            : (C) 2024 by Karolina Chankre, Milena Cieślak
        email                : 01179115@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PROJ_INF_2_v2 class from file PROJ_INF_2_v2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PROJ_INF_2_v2 import PROJ_INF_2_v2
    return PROJ_INF_2_v2(iface)
