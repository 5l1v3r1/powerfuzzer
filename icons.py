# Powerfuzzer
# Copyright (C) 2008 Marcin Kozlowski

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  US

from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO


#----------------------------------------------------------------------
def get_rt_alignleftData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00BIDAT8\x8dcddbf\xa0\x040Q\xa4\x9b\x81\x81\x81\x85\x81\x81\x81\xc1\
\xc7\xdb\xeb?9\x9a\xb7l\xdd\xc6\xc8H\xa9\x17Hr\xc1\x96\xad\xdb\x18\xd1\xc5\
\xe8\xeb\x02l.\x1a\r\x83a\x11\x06\x14g&\x8a\r\x00\x00\x90v\x18Pe\xb5\xde\x18\
\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_alignleftBitmap():
    return BitmapFromImage(get_rt_alignleftImage())

def get_rt_alignleftImage():
    stream = cStringIO.StringIO(get_rt_alignleftData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_alignrightData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00<IDAT8\x8dcddbf\xa0\x040Q\xa4\x9b\x81\x81\x81\x85\x81\x81\x81\xc1\
\xc7\xdb\xeb?9\x9a\xb7l\xdd\xc6\xc8H\xa9\x17X\xb0\t\x12\xeb"\xea\xb9`4\x0cF|\
\x18P\x9c\x99(6\x00\x00\xd0g\x18P\x14m1\xc6\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_alignrightBitmap():
    return BitmapFromImage(get_rt_alignrightImage())

def get_rt_alignrightImage():
    stream = cStringIO.StringIO(get_rt_alignrightData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_boldData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00KIDAT8\x8d\xcdRA\n\x00 \x0c\xca\xad\xff\xff\xb8\xd65\x0c\x16cA\xf3(\
\xd3\x89\x08\x88\xb6\x0c$\xa5~a\xd0\x99\xb09\xcc\x13@\x14n\x02>\x80(v\x8e\
\x1f\x14\xec\x80\xc1\x91\xaf\x1d0\xeaw\x00\x9ert\x07\x87A\x14\xff;H\x1b,\xb5\
t\x14I\xb8\x7f\xfd3\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_boldBitmap():
    return BitmapFromImage(get_rt_boldImage())

def get_rt_boldImage():
    stream = cStringIO.StringIO(get_rt_boldData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_centreData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00BIDAT8\x8dcddbf\xa0\x040Q\xa4\x9b\x81\x81\x81\x85\x81\x81\x81\xc1\
\xc7\xdb\xeb?9\x9a\xb7l\xdd\xc6\xc8H\xa9\x17X\x909\xc4\xbad\xcb\xd6m\x8c06u\
\\0\x1a\x06#>\x0c(\xceL\x14\x1b\x00\x000v\x18P\x0f8\x82\xa8\x00\x00\x00\x00I\
END\xaeB`\x82' 

def get_rt_centreBitmap():
    return BitmapFromImage(get_rt_centreImage())

def get_rt_centreImage():
    stream = cStringIO.StringIO(get_rt_centreData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_colourData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00\xf6IDAT8\x8dcddbf\xa0\x04\xb0\xe0\x92\xf8\xc7.\xf6\x1f\x9b8\xd3\xcf\
W\x8c(|B\x9a\xdf\xb2\xf3\xe35\x98\x11\xdd\x0b\xb8l\xc6\xe5\x12\xac. \x05\x0c\
B\x03\x96T\xf31lm\xc8bx\xca%\x8a\xa1\xf8\x1f\x0b$\xd2\x90c\x02%\x10\xdd\xfe\
\x1a\xffg````\x99\xe5\xc0 \xf2\xfd#\x83\xef\x82\xf7\x0c\xba\xcf\x1f2\xb0\xfd\
\xfb\xcd\xf0\x98]\x81a\x83X0\xc3\xe5_Q(\x86\xc2\r\x80i\x16\x7f%\xc3\xf0\xea\
\xfd\x1f\x86\xff\xea/\x188\xbe\xfdc\x08\xeb\xf9\xcc\xf0of\n\xc3J\xe9 \x86\
\x9f?e\x19\x18\xfe\xb1b\x1a\x00\xd3\x8c\x15|\xe2e\xf8\xe7\xbd\x96\x81\xe93/\
\xc3\xbf\xbf\x98A\xc6\x84W3\x03\x03\xc3\xff\xb7B\x0c\x0c\xffp\x875\xe1X\xf8\
\xcb\xcc\xc0\xc0\xf2\x13\xab\xedD\x19\xc0(\xfa\x96\x81A\xf69\x05.\xe0\xff\
\xc8\xc0h|\x1e\xb7\x05\x04\x03\x91\x81\x81a\x17\xf3YF\x17\xad?X\xd5\x00\x00\
\xac\x08RO\x1e0;\xef\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_colourBitmap():
    return BitmapFromImage(get_rt_colourImage())

def get_rt_colourImage():
    stream = cStringIO.StringIO(get_rt_colourData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_copyData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x019IDAT(\x91\x85\x93\xbdN\xc30\x14F\x8f\xed\xa4M\x80v(b\x00\t\x90X\xd8\x8a\
X\x80\xa9\x0c\x88g@H\xbc\x03O\x80J\xc5\xc0\xcc; !\xc4\xc4\x03t\x006\xc6n]3\
\x10\x06*\xa4RAE\xd3\x86\x81\xda\xc4IH\xeftm_\x9f\xfb}\xfe\x11B*\xce\xae\xdb\
1\xa9\xb8\xefU\x00\xe8\x9c\xee\x88\xf4Z2\xa4N\x96\xd76)/m0XX%P+\x00\x9c7\xd6\
\xa9_=g\xe0\xb9\x80\xaa\xa7\xa8\xf9.\x8b\xbeK\xcdW\xa6`\x16Dh\x0b{[u\xde\xbf\
"\xfa\xc31a\xd0-j\xca\xc5\xc9\x81\xb1\xe5\xe8\xa4\xe2\xfdu\r\x81\xd6\xf1>\
\x9d\x97O\xfa\xc3\x88\xb7\xc1\x88\xd7\x8f\x11a\xd0\xa5y\xd4\x00\xda\xb1\x86\
\x18@\xd53)yP\r\x06,\x88\xd9\xe5\xbb2\xc9\x03\xa0\xac\x04\xa4 \xad\xdbGklv\
\xcc\x97dz\x8a\xb9\x92\x82\xef\xb1\x81\x1c\xeen[v\xacjG\t<W\x90\xb8\x18\\%\
\x0c$J)\xd4v\x12\n\xb4\xd4\x89)R\x12`\n\xc9\x8a\xb6GJ&!\xd39!@\xc6\x85\x90\
\xec\xd1[\x80_\x05\xf9\x90\x14\xe0\xf2\xee)\xb3(\xa5\x80I\\\x08q\xc0~Y\x80\
\xf5\xb9fA\xfe\xb5\xd0\xbcy(rg\xe2\x07P\xd3Y\x1e\x1a\xf3j]\x00\x00\x00\x00IE\
ND\xaeB`\x82' 

def get_rt_copyBitmap():
    return BitmapFromImage(get_rt_copyImage())

def get_rt_copyImage():
    stream = cStringIO.StringIO(get_rt_copyData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_cutData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x01\xb0IDAT(\x91\x9d\x93AK\x1bQ\x10\xc7\x7f\xef\xa5\x17o\xee\xc1\xb8\xf4"\
\x98\xc6\xf4\xa6T<$\xa5\xde\xfc\x00\xb6\xd2J\x14$mO5\x82\xe0\x07\xf0\x13x\
\x10M\n\x1aP\x90\xe6 \x08\xa2&\x88\xc1`\x0f\xdd\xb8\xb4YvK[Z\xb6Y\xf1\xa6\'\
\xc9\xa1W_O\xbb\xecjZ\xc4\x81\xc7\xf0f\xfe\xf3\x9b\x99\x07\x0f!c\xf8\'?7\xaf\
\xde\xafo\xaap,\x9cs]\xf7VN\x12\xb2\xb8\x94|\xffj\xe38\x8e\n\xc7?\x19\r\x050\
\x90z,\xb8a\x11\xc0\xe2\xca\xb2\x88K\xc9\xdaZ)"*\x7f(\xdf\xac\xeb\x0c\xf0-\
\x95JR\xab\xd5\x14@\xb5RQ\x00\xaf&\'\xef\x06X\\Y\x16Wn\x8b\xdd\xdd=<\xefLU\
\xaa\x87\x00\x8c>{zk|\x80\x07\x9d\x82Z2\xc1H"\xc1\xc1\xc1\xfe?G\xff\xef\nWn\
\x8b\x8b\xcb\x0b\xf2\xb3\xef\xee\x07\xd0\x92\t\xf4^\x9d\xd5B\x91\xec\xcc\x9b\
\xfbM\xf0\xf9\xf0\x88\xa1\xc1A~}k\x12\x97\x1de\x00\x08!c\x00|\xa9\xd7\x95W\
\xda\x02 m\xd842C\xbc,o\x88\xedlN\xf9w\x80G\x0by\x9e\x0c\x0f\x07\x0f*\xfd\
\xe2\xde\xd7\x0bH\xef\x9c\xb6\xe5\x04\xc2\xb0o[\x0e\xd2;\xa7\xe7\xc5[\xacfSE\
\x00^i\x0bS\xd7\x988\xad\x0b5\xfd\x1c \xe8\xe2\xfb\x87\xb39&N\xeb\xc2\xd45~/\
\xadF\xdf m\xd8\\\xf7\xf7\x01\xd0\xfd\xa3\x85\xa9k\x91=M]\xe3O\xc3\x02\xe0\
\xba\xbf\x8f\xb4aG\x01\xa6\xae\xd1\xb6\x1c\xfc}\xbb\xa6\xc6#\x80\xae\xa9q\
\xd2\x86\xcdv6\xa7\xda\x96\x13m d\x8c\x9f\xc7\'j\'3\xa6v2c\xaaZ(v\xfc\x8d\
\xd5B1\xd04O>\x06\x9a\xbfO\xcc\xa84\xa1\x9d\xc6\x7f\x00\x00\x00\x00IEND\xaeB\
`\x82' 

def get_rt_cutBitmap():
    return BitmapFromImage(get_rt_cutImage())

def get_rt_cutImage():
    stream = cStringIO.StringIO(get_rt_cutData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_fontData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00\x8aIDAT8\x8d\xb5\x93\xc1\r\x80 \x0cE)\x8c\xa7\x0c\xc0\x81\xe9\xd4\
\xb2\x00\xcc\x87\x07\x82\x81JQ$6!$m\xfa\xda\xff\x03\x00R\x89\x99\x90S\xddo\
\x00\xeb\xb2\xc5\xcf\x80cO\xcd\xf9\x1e\x068W\xdfC\x00:\x95\xdb\x82\x05\xe4\
\xa9>X\xe8m\xd1\x04\xe4i\xb9\xb9\xb7\x05\xb4\xdeA\xcfy\n\x15 Uu\x101j\x8d\
\x91\xe6\xb5Ny\xc4\xbav\x93\xc0i5\xa6]\xaf\x00\x9cv\x1a\xa5\x17\x97\x07Tw\t\
\xe1<\xf1\xc1B\xd3\xc4\x91\xf8\xff3=\xc5\t\xa2\xed@\x80\nB\x85Z\x00\x00\x00\
\x00IEND\xaeB`\x82' 

def get_rt_fontBitmap():
    return BitmapFromImage(get_rt_fontImage())

def get_rt_fontImage():
    stream = cStringIO.StringIO(get_rt_fontData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_ideaData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x01[ID\
ATX\x85\xed\x97aN\xc2@\x10\x85\xdf.\xde\x00\t\xa7Q\x17\xb9\x01\x01\xaec\x94\
\xdb\x80\xf1\x06\xda\x16\x8e`<\x04\tW\xb0\xeb\x0f\\\xd8\xdav;oD\x89\x89\xefO\
\x13\xa6t\xbe};\x9d\x9d\x1ac{8\xa7.4\x7fZ\xaeJ\xff\xf5\xb7\xf9\xcc\x1a\xcd\
\xb3\x0c\xe3@H<\x9d\xdc\xd4b\x8fO\x85\nD\x04\x90J\x1ck\xbb+\xb0Y\x83\x02\xe9\
\x04X\xaeJ_M\x9c\x01\x18%!\x00`\xb3\x96AX\t\xe51q5\xb91\xaev\xd7\xf02\xed\
\x12\x05p\\}V\x8b\x85\xe4M\x10\x00pu\xdd\\\xac\x14@]\xed\xd6\xc7b\\h\x05H\
\xad^\n!q\x81p@\xb6zV\x82F\xa4O\xbc\xdf\x8a"y\x0fY\x03\x9c\xc2+y\x16\x00I\
\xf2$\xc0|fMh\xafZI\x9a\x91\xda\x01\xef\xf3\xcaU+E+\xeeV8\x13$\xadXu\x1c\x03\
\xd5\x0e\x18\xbb \xdd\xfb\xa0\xce-`j\x81=\x88\x00b\x1e\x90l\x05c}\x10U\x84)\
\'\xe2Y\x80\x91\x18 \xb5*\xcd \x12D\x15\xe1\xdb\xeb\x1d\x06}\xd7\x18\x1b\xf4\
\x81<\xcf\x01,\x98G\xf2o\xc1>\xc9\xe9D\x038\xe7Zc\x1a\xb8\x7f\x07(\x80\xfb\
\x87\x85\x01\xd0:\xe1|\xc6)Q\x1f&\xb1\xb2\x97\xe7\x03\xc8\xe8v\xac\xfa*\xfa\
\x16\x80/\xdf\x0f\x00\xc6\xf6~\x1f\xe0T\xfa\xd1\x91\xecO\x00|\x00\x0e\x85\
\x8c7\xc5\x108|\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_ideaBitmap():
    return BitmapFromImage(get_rt_ideaImage())

def get_rt_ideaImage():
    stream = cStringIO.StringIO(get_rt_ideaData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_indentlessData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00tIDAT8\x8d\xcd\x92o\n\x80 \x0c\xc5\xf7\xb6NW\xed\x08\x9d.\xe8\x04\
\xda\xf5\xec\x93"\xa6b)\xd1\x03a\xf8\xf6\xe7\xe7\x90\xc0B\xa5\xa3\xaa\xae\
\xe6\x83\x85\x00\x16\xea\xd1\xe4\x83u\x99]l\x18{"\xbd\xcbi$\xc1\xee\x8c\xdd\
\x10\x9b-\x04\xec\x8b\xdf\x12@\xf5\xb8\x15\xa7$\xd5\x06`\t\x04\xadO0\xf6\x0c\
y\xfctb\x96\xa0G\xbf\xfa\x07e\x82xi\xc3\t\xb8f~\xb2\x83\x0b\xf1\xae.\x0fLGF\
\xad\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_indentlessBitmap():
    return BitmapFromImage(get_rt_indentlessImage())

def get_rt_indentlessImage():
    stream = cStringIO.StringIO(get_rt_indentlessData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_indentmoreData():
    return \
"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00yIDAT8\x8d\xcd\x92a\n\x80 \x0c\x85\xb7\xd9\xe9\xaa\x1d\xa1\xd3\t\x9d\
\xc0y=\xfbeLM\x93\x92\xe8\x81 >\xdf\xf69\x04$\x03\xb5\xc5\xcc\xa1\xe5#\x19@$\
\x03o4\xc5\xcd\xba\xccA\x1bN<\xe6gW\x1aI`\x83\x93\r\xb5\xd9C@i\xc0\xde\x06r!\
\xf3^\x84r\x92f\x818\x83\xd8]\x87kOp\xe2\xcf;\x94\x1a\xfd\x9d\x0b\x82\xa7\
\xfa\xd5?\xa8\x13\xe8\xa1\r'\xa0\x96\xf9\xc9\x0c\x0e\xc1\xae.\x0f\xf2\xb3\
\x80G\x00\x00\x00\x00IEND\xaeB`\x82" 

def get_rt_indentmoreBitmap():
    return BitmapFromImage(get_rt_indentmoreImage())

def get_rt_indentmoreImage():
    stream = cStringIO.StringIO(get_rt_indentmoreData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_italicData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00gIDAT8\x8d\xd5\x93Q\x0e\x800\x08C\x0bx\xffc\xf4\x96\x8a_K\xa6\x0e\
\x82\xc1\x1f\x97\xecg\xb4\xaf$0\x115t\x8e\xb6\xdc_\x00\xb6\xac\xe8\xc7\xee\
\xf77Q\x93r\x07\xb3\x98\xe4\xc3<D\xe1%\xe9\x00\x1c\x80G\x9a\x140\xcc$\xdf\
\x03*\xe9)\xa0\x92\x1e\x02\xaa\xe9!\xa0\x9a.j\x90y\x95Ws_\xcd\xfeR\xfb\xff_h\
\x03N\xae\x87)\x94\x8d\x1e\xc5*\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_italicBitmap():
    return BitmapFromImage(get_rt_italicImage())

def get_rt_italicImage():
    stream = cStringIO.StringIO(get_rt_italicData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_openData():
    return \
"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x01\xbaIDAT(\x91\xa5\x93=H[Q\x14\xc7\x7fW\xdf3Q\x83\x01A1\xa0\xa8CK\x05'\
\x07\xe9 (\x01q\xc8$A\tN!E\x84\xd2RBU4\xb4)hT\xd0\xa8X-\xe8\xa0\xa0\x83\x1aA\
p\xb0\x83\x1fXGu\xe8 -\xa5\xa5\x83.\xe2\xe2\xe0\xd3\xf8\xf2\xf2\x02\xcfA\xf2\
\xf0\x19\xe3\xe2\x99\xce\xfd\x9f{~\xe7\xe3r\x85\xc8\xc9\xe59&=&\xd6\x07\x06\
\x8c\xfb\xe7\xa3\x85\xb0\xc8\n\xa8\xf2\xf6\x1a\x0f\xc5\xa3\x85\xb0\xa8\x0f\
\x0c\x18\xabQ\x0f\x00>0\xb2A$\x80w\x9e&\x8b\xb8UQfD\xfc\x1e|\xdd1\xa6\xc3/X\
\x8dz\xb2BDu[\xbf\xf1\x10\xa0h:\x8ar\xc5u\xe2\x86\xe3\xd3s\xbe|tP\xe3j\xc4\
\xdd\x193\xef\x9c\xac\x8f\n\x80\x9c\xc7\xda*\xb2\xc9\x94\x97\x14\xf3\xaa\xa2\
<#6\xfd\xa1#s\x04\x80\x99\xef\xfb\x96@\xa9\xd3a\xfa\xaa\xf1\x07h\x04\xe0\xfd\
\xd42\x00U\xde^\xa3\xb6\xd2e}\x85\xafo}\xd8e\x19\x9bM\xa6gn\x8d7\xc3?\x01\
\xb8\x00v\x92\x83\xf4\x7f\x83\xe6\xbc\xcf\xb8;c\xfc]\x19\xc2\xdb7s7\x82\xa2\
\xaa\x00\xc4U\x8d\x84\xae\xa3i:c]\xed\xcc\x87\xea,]\xa5\x93\x7f-\x86\xd9>\
\xf8\x8d\xb9\x83\xa5\xbdC\x02-\r\\\xdd$,\x90\x88\xbf\xd5\x84\xa4\x93\x0fgChz\
\x8a\xb9\x8d\x1flN\x04\x859B\x81$\xa1i\xba\xa5\xa2]\x96\x89\xf8[\xf9\x14\x82\
\x91\xcb\x18;\xe3A\x92\xa9$\x90g]\xe2\xeb\x97\xd5(\xaaJ\x11\xf9\x19[OC\x9c\
\xc5\x85\xc4\xd5\xbb\x02\xffN\xcf\xac\x00\x87=\x17]K\xa1\x90\x1d\x92\x88'\
\xa1\x10Parm\x8b\xcd\x89\xa0\x00\x90\x9c\x05vv\x8f\xffg$=e\xb5\x95.\xd3\x17\
\xcf\xfd\x8d\xb7\xd2\xb4\x9d\xba\x05\xf7F\xcb\x00\x00\x00\x00IEND\xaeB`\x82"\
 

def get_rt_openBitmap():
    return BitmapFromImage(get_rt_openImage())

def get_rt_openImage():
    stream = cStringIO.StringIO(get_rt_openData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_pasteData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x01sIDAT(\x91\x85\x93;/DA\x18\x86\x9f\xef\xcc9\xd6X{\xb1v{\t\x8d\xdf\xb0D\
\xa3\xd8\x82B\x14*\xa1\xd5*\xd6%B\x88\xb8\x15~\x81\x88d\x13\xa2Q)\x14\x12\
\x14\xfe\x05\t\xb5\xb5\xd6u#.\xa3X\xc6\x1e\xe7\x9cx\x9b\xc97\x99\xef\x99\xf7\
\xfd&#\xe2(~\x94/\x96\x0c!:\xdf\x18\x95\xb0}\x00\x11G\x91/\x96\xccX\xf2\x9a\
\xab\xea\x0b\xcb\xebK\xbe\x03sS\xf3\x00\x9c9\xdd\xa1 \'_,\x99\x93\xfeO\x80@\
\xf3\xcf^G\xba\x85\xc3\xf6\xe3P\x87nc\xb1\xb5\xba\x16\xe54R\xd23\xbdkN\x873\
\x98\xfb2\x00\x1f\x95\x1b\x00\xccM\x8d\xd7\x97\x0b\x06n\xfb\x03M\x8dQ\x1cKJe\
\x01P\x99\\\xbd\xceib-]\x00lN\x0c2;Z\x00\xe0hq\xc4\x17\xc5\x01\x90D[$\x04 \
\xad]\xb2\xad\x9eu\xd0\x08\xb13\x90D\x1b\xe6\xf1\x0eIe1\xf7eT&g\xe3\xa4\xf4\
\xefS\x17\x16\xf6}q\\\x00\x89\'1\xcf\x0f\xa1\x10\x80&\xe5\x90\xd2\xb0=9D\xb5\
\xf6N\xf9\xe9\x8d\x95\xd2\xd1/\x00\x9d@ \x14\x02\xd0\xec\tP\x87\xfc\x95\x1d"\
:\x81\xc4\x936\x8eo&"4{\xf2\xedD\x91\xd6\xae\x1f \x9e\x8e\x84\x00xJ,$\xde\
\xa4|3\xa9\xa3b1\xc4U\x98\xdaS \x0eT\xe8\x9d\xd9\x0bz\xf7\x01\x9c\xfa"\xba\
\x15\xde?0`!g\xe3\x9d\xf6p\xdf\xcee\xe0?\xb8\x00\xbd\xf3\x07\x917\xfc\xa7/\
\xbf\rv\xe9ib\xe3\x0c\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_pasteBitmap():
    return BitmapFromImage(get_rt_pasteImage())

def get_rt_pasteImage():
    stream = cStringIO.StringIO(get_rt_pasteData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_redoData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x02\x0eIDAT(\x91\x9d\x92\xbfkSQ\x1c\xc5?\xf7\xbd\xbc\xf6\xbd\xf4\xbd\xdb\
\x8a\x91\xa6j)Vb,\x14%\x83\x88Y\x02\x01q\xec\xe4 \xe8&\xa4\xab$\x83\xfe\x05.\
m\\,4\x10p\xe8\xe0PT\x82\xe0\xe0P\xb5P"bI-\xed\x10\xbbhj["\x8d1?j\xd2\x9f\
\xd7\xa1\xf4G\x9a\xda\xc1\x03\xdf\xe5\xdcs\xcf=\xf7\xdc+\x84\xa6\xb3\x87\xf1\
\xc9\x19\xf545\xc5b\xa1\xb4\xcf\x85\xaf\xfaH>\xb8-\xf8\x07\xc4\x9eA4\x91R\
\xaf\xd2\xf3\xb4\x9b-M\xa2R}\x83\xeb\xfen\x9e?\xba\xd7`\x14M\xa4\x94\x10\x9a\
N\xfc\xe5{5\xf6\xf63\x1eS\x03`}[\xa3\xb2\xb9\x85c\xb8h\xd5w\x1a\xb8\xcchL\
\x1c>P\x08M\'\x14\x1dQ\x1e]a\xe8:\xd9\xe2\x1a\xe1\x80\x8f\xfe\x9eN\xe6\xbe\
\xe7\x99\xc8,\xd0+M\x0c]\xa7R\xdfa\xb9V\xe3rO\'K\xcb\x05*\x9b[\xb8\x00\xcak5\
|]\x92j}\x9bp\xc0\xc7pd\xa0\xf1\xce\x83C\xca\x7f\xaa\x8d\xae\x0e\x03\xc7\xd4\
\xd8(\x96\xb8\xe4q3\xbdRF\x03p\x0c\x17\xb6\xe9\xc66u\xce\x9dio\xea 3\x1a\x13\
\xd9\xe2\x1a\x00\xde\x0e\x87\xee\xd3\x1d\xd8\xa6\x1b`7\x01\x80\x94\x0e\xd2\
\xb6HM\xcd\x1f\xdb\xb6l\xb3\xb0M7R:\xfb\x9cc\xac\xee\x1a\\\xeb\xbf@\xb5^\xe3\
\xac#\xf1\xb44\xbfX`pH\x85z\xbdH\xcbjZ\xd3\x00\x86#\x03b:W@\xda\x16\xb7\x02}\
\x84\xa2#jOp\xe7\xf1\x98\x02X\xc8\xaf\x92\xfb]\xa0\\\xab!m\x0bi[\x88\x16\xe3\
\xe0\x1f\xdc\x7f2\xae\xa4\xb6M\xd0\x7f\x91_\xe5*\xcf>~%\x1d\x8f4\xc4\x19\x9f\
\x9cQ\xd9\xc5<\xf3\xb9\x9f,-\x17\xf8Q\xf9s`\x00p\xf3aB\xdd\xbd\xd1\xc7\xf9N\
\x0f+\xf9"#\x1f\xe6\x9aL\x9a 4\xbda\x82\xb1\xa4z11\xabf\xb3\xdf\xd4\xebw_T0\
\x96TG5\x87G;j\x98\x8eG\xc4\xf0\x9bO\xac\x96\xd6\xb9\xe2\xef&\xe8\xf7\x9e\
\x18\xc0u\x1c\x99\x8eGD\xdcN*i\xb5\x9e\xb8\x19h\xec\xe0\x7f\xf0\x17QL\xb6\
\x0e:\xc2\x0cm\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_redoBitmap():
    return BitmapFromImage(get_rt_redoImage())

def get_rt_redoImage():
    stream = cStringIO.StringIO(get_rt_redoData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_sampleData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00\
\xc3IDATX\x85\xed\x97K\x1a\xc2 \x0c\x84g(7i\xaf\xa8\x87\xa8W\xa4GQ\\(\x0b\
\x95j\x88\xe9\x17\x16\xcc\x9a\x84\x9f\xbc\x002L\xf0Tp\xdd}\x00\xf4\x00\x10\
\x7f-\xc8\xb7k\xd68f\x98h\x02\x00\x00\xf3|j\xda|\xdb.\xe2\xb5\xee)\x10\x03\
\xa4\xb4"\xa5\xd5\x0f\xe0(\xb9\x03\x88\x8aP\xa2\xf7\xc2\x93v\x8f\x19\x00\x00\
\xe4\xc6\x86%\x81\xa8\xeds+E\x00\xf8F \x9a&/*\xded\x96\x1d\x15aI \xeb\xe4\
\xcbr>\x04\xc0=\x02D9\xfbN\x04Zj\xe0\xe9HlIJn\xc3\x9a!>o;m7\xb9\xa7\xc0\x1d\
\xc0t\x12>\xd469:\x8a\xc0N\xff\xb7H\xe3\xc2,\x05\xd27`\x15\xe0\xff\xb3\xeb\
\xc5\xf15\x1b\x00\xde\x00w\xa7\xdb(\xe7d\x95\xec\xc5\x00\x00\x00\x00IEND\xae\
B`\x82' 

def get_rt_sampleBitmap():
    return BitmapFromImage(get_rt_sampleImage())

def get_rt_sampleImage():
    stream = cStringIO.StringIO(get_rt_sampleData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_saveData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x01\rIDAT(\x91c\x8cO\xcb\xfd\xcf@&X4g\x1a#\x0b\x03\x03\x03\xc3\x9e{\xbf\x18\
\xbc\xec\xcd\x18f\xd5$\x11\xd4\x14W;\x85a\xdf\x89+\x0c.Jl\x0c\x0c\x0c\x0c\
\x0c,\x0c\x0c\x0c\x0c\xf1>\xae\x0c\xaf?\x7fd````\xd8\xbbo?N\xcd\xceN\x8e\x0c\
0\xf5O\xaf\x1dD\x18\x80M\x11\xb1\x00\xc3\x00b\\\x80\xd7\x00\xb2] \xca\xcb\
\xcf\x10W;\x85\xa0\x06Y\x11I\xdc.@\x97$\xc9\x050\xb0\xed\xfcU\xbc\x1a\xbc\
\x0c\xb5q\x1b\xb0\xed\xfcU\x86\xd2@K8_\x88\x9f\x97\x81\x9f\x97\x87\x81\x87\
\x97\x97\x81\x9f\x97\x8fANR\x90\xc10\xa1\t\xc5\x10\x0c\x170000\x94MY\xcb\xa0\
\xa9\xa6\xca\xc0\xc0\xc0\xc0\xd0\x94\xe4\x8e\xd7ELxe\x19\x18\x18~\xfd\xfe\
\xc7\xc0\xfc\xf7\x07\xc3\xef?\x7f\xc83\x80\xf9\xdfw\x86\xaf\x7fX\x18~\xfd\
\xfd\x8bU\x1e\xc3\x0br\xa2|\x0c+\x1a\x13\x19\x84\xa5\xe4\x194\x15$\x08\x99\
\xcf\xc0\xc8\xc8\xc4\xcc\x10\x97\x92Er\x8e\\4g\x1a#\x03\x03\x03\x03\x00\xb7\
\xa8?\xb7)\xf6\xbb\xdc\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_saveBitmap():
    return BitmapFromImage(get_rt_saveImage())

def get_rt_saveImage():
    stream = cStringIO.StringIO(get_rt_saveData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_smileyData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x01:ID\
ATX\x85\xedW\xd1\x16\xc2 \x08E\xd7\x87\xed\xd3\xf7cE\x0f\xc6"\x07^4w\xd6C\
\xbcT\x83\xee\xbd\x03EL)/t\xa5\xddF\xfe\xc4\x8f;\xd7\xcfR^\xd2\xa9\x024)\x1f\
\xe8\x89Rz\xfb{\xc4$T\x02!\xb6H}\xd0\xb8\x90\x8c\xc8\x99\xfb\xc8\x89J<\xb3]\
\xaa\xda\xcc\x0c\x8c\xbc\xb5O\xf0\xfat\xb2\xe1f`\x06\xb9\xe0\xb4\xb2q\x10 i\
\xb7,\x81\x8a"?\x14\x80\xc8\x99}\x12\xe4\xf7\xb2\xd0\\\x845\xb8\x00\xd5$\xc8\
\xdf\x12\xb1\x0b\xf0\xde^\x83k \xf4;Z\x0e\x98\x01\r\xde\xb3\x06\xa2\x8b8T\
\x823-\x13\xb5\x17\x9f6\x14\x13\xc5\xd0\xeb\xe072\xf0\x17\x80\xac\xb7\xc3\
\xf5\xc4g\xa2rPD\xb6\xd8\xb4\x18u0\x85\x07\x92M\x01\x10\xd9\xfdAb\xd6(hT\x80\
t\xb6\xcd\x10\xa2\x89\x85\xbcoxQ\xf3\x00\xea\x07"\xc2\xb3\x08\xf9p\t\x88>{\
\xbc\x16\xb2*\x7f\x0fyyVMD\xd1\xae\xd8\xdb\xf7-r"c\x1bFv\x84\x90\x8e\xcc\x8b\
P\xc0.dh\xca\xb7q\xbc\xb7/\xfe\xc6X\x1e-G\x93\x1c\x8c\xe6\xcdN(\xe5\x18\xe9\
\x84\x11\xf2\x12\x1b\xbc\x1b\xe2\x9b\x91\xfa>\xf3f\x84\xc4\x8c\x90~-`\xa6]~\
\x1c?\x01\xdf=\xae\x9f\xe1\xb5v\x06\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_smileyBitmap():
    return BitmapFromImage(get_rt_smileyImage())

def get_rt_smileyImage():
    stream = cStringIO.StringIO(get_rt_smileyData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_underlineData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00WIDAT8\x8dcddbf\xa0\x040Q\xa4\x9b\x1a\x06\xb0\xa0\x0b\xfc\xff\xf7\
\xf7?2\x9f\x91\x89\x99\x11\x9b\x18N\x17 K\xc2\xd8\xd8\xc4p\x1a@*\x185\x80\
\x80\x01K\x97,\xfe\x8fLc\x03\x8c\xb8\x922z\xdc30`F!^\x03\x88\x05\x04S"6\x80\
\x92\xb0\x06<7\x02\x00\xcev\x16+\x82\x11y\x82\x00\x00\x00\x00IEND\xaeB`\x82'\
 

def get_rt_underlineBitmap():
    return BitmapFromImage(get_rt_underlineImage())

def get_rt_underlineImage():
    stream = cStringIO.StringIO(get_rt_underlineData())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def get_rt_undoData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x0f\x08\x06\
\x00\x00\x00\xedsO/\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x02\x15IDAT(\x91\x8d\x92\xcbk\x13Q\x18\xc5\x7f3\x99\xc4\x99d2i\xda\xb4\x8d}\
(6\xd8 \rb\x16"\x8dh\xc0\x8d\xcb\xe2\xc2Eq[hAW&\x7f\x81\x9b\xbah\xebJh\xb0\
\xbbv\'*\xc1\xc7F\x88\x8a\xd4\xa0"!\xa5EC\xb0\xf6a\xab\x81\x846\xa16iK\xb9.\
\xea\xa4/\x1b\xfd\xe0[\xdc{\xcf9\xf7\xdes>I\x92-\x1cU}\xf7\x1e\x8aD:[]\xb77\
\xb8\xb8\xd5s\x91\xeb\x97\xcfI\xe6\x9e\x14}\xf0L\x0c\xf7\xf7H{\x89\xbd\x83\
\xe3\xe2}f\x11\x97j;$Z\xaclr\xad\xbb\x0b\x93#?I\xce\x10\x89\xc5\x85\t\x08\
\x0e\x0c\x89\xa5\xe5\x02\xbe:\x15\x8f*\xe3\xb4*\x008\xad\n\x1eU\xc6W\xa7\x92\
He\x19y\xfcZ\x00(.\xd5\xc6\xc7\xe9o\xf4\x0e\x8e\x8b/\xf39Z4\r\xa7*\xb3\xb5\
\xbd\xcdl\xa9\xc2\x95\xa0\x8f\xc0\xc9f\xa6\xe7s$RY\xfcn\x07\x86m\x9b\xf8\xe4\
\x0c\x00\n@\xa7\xc7\xce\xcaJ\x11\xbf\xdb\x81\xaeZX\xab\xec\x90S\xa3Q)\xb5\
\xe7\xf9\x91X\\,\xcd-\xe3v\xd8\x98\xfdQ\xda\x15\xd0U;\xbaj\x07`\xad\xb2Nf\
\xe5\x17\xa9\xd1\xe8>_\x00Z\x1b]\x14\x7f\xe6\xd0U;N\xeb\xfa\x8e\x80\xd3\xaa`\
\x18\xce}@\xc3\xb1\xf5\xd7T\xe2\x933\x84;\xbc +@\x1e\x00\x19\xc08f\xadv[c=\
\xe1\x0e/\xc1\x81!qP\xc0c\x9304\x8d\xb5\xcd2\xe7\x03\xa7v\x04$\x9b\x15C\xd70\
t\x8dR\xb9\xcc\xc2j\x81l._\x8d\xd3$\x87#\xf7\xc5\xd5\xe0\x19\x0c]\xe3\xd3B\
\xa1\x1a\xa3\xb2X(2\xf16MkK\x03]\'\x9a\xb8\xd4\xee\xab\x0e\x8ai`\xf7\xed\x98\
\xb8q\xa1\x93zC\xe7]\xe6+\xa7\xdb\x9ax\xf3\xe7L\xaa5\x89&\xf9f8\xc0\xf1f7\
\xdfsy&\x92\x9fyy\xb7\x7f\xd7`I\xb6\x1c\xd9\xa1\xe8\x98x\xfa*-\xa62s\xe2QbJ\
\x84\xa2c\xe2 F\xaeu{\xc8\xef\xe5\xac\xbf\x9d|q\x83\xe1\x17\x1fH\x8e\xf4\x1f\
\x8a\xb6\xe6\x17L\x13K\xe5\r\x9e\xdf\xe9;D\xfe/\x0f\xfeU\xbf\x01\xf6\t\xb0_}\
e\xc8\x99\x00\x00\x00\x00IEND\xaeB`\x82' 

def get_rt_undoBitmap():
    return BitmapFromImage(get_rt_undoImage())

def get_rt_undoImage():
    stream = cStringIO.StringIO(get_rt_undoData())
    return ImageFromStream(stream)


