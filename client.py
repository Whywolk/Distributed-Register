#    This file is a part of Distributed-Register source code
#    Copyright (C) 2021  Authors:   Alex Shirshov <https://github.com/Whywolk>
#                                   w0rest <https://github.com/w0resT>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from client_app.client_gui import ClientApp

if __name__ == '__main__':
    app = ClientApp()
    app.run()
