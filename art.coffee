# Copyright (C) 2018 Mitchell Manguno

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

command: "curl --silent http://127.0.0.1:5000/"

# the refresh frequency in milliseconds
refreshFrequency: 1000

render: (_) -> """
<img id="album_art" class="album_art" src=""/>
"""

update: (output, domEl) ->
  if !output?
    $(domEl).find("#album_art").css("visibility", "hidden")
  else
    parsed = JSON.parse(output)
    link = parsed["link"]

    if parsed["playing"]
      height = parsed["height"]
      width = parsed["width"]

      # set the art in the img src
      $(domEl).find("#album_art").attr("src", link)
      $(domEl).find("#album_art").css("visibility", "visible")

      # put the art right in the middle of the screen
      # src: https://sayzlim.net/change-ubersicht-widgets-position/
      $(domEl).css("margin-left", width/-2)
      $(domEl).css("margin-top", height/-2)
    else
      $(domEl).find("#album_art").css("visibility", "hidden")


style: """

  border: none
  background: none


  img
    border: none
    border-style: none
    background: none

  top: 50%
  left: 50%

  album_art
    height: 100%
    width: 100%

  font-family: Iosevka
  font-size: 12px

"""
