# Volatility
#
# Authors:
# Mike Auty <mike.auty@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#

#pylint: disable-msg=C0111

import volatility.commands
import volatility.win32 as win32
import volatility.utils as utils

class Sockets(volatility.commands.command):
    """Print list of open sockets"""
    def render_text(self, outfd, data):
        outfd.write("{0:6} {1:6} {2:6} {3:26}\n".format('Pid', 'Port', 'Proto', 'Create Time'))

        for sock in data:
            outfd.write("{0:6} {1:6} {2:6} {3:26}\n".format(sock.Pid, sock.LocalPort, sock.Protocol, sock.CreateTime))


    def calculate(self):
        addr_space = utils.load_as(self._config)

        return win32.network.determine_sockets(addr_space)
