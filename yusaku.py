#####################################################
# ゆうさくメーカー
# Ver. 1.0.0
#
# ゆうさく注意喚起シリーズを簡単にLINEに貼り付けられるように制作した
#
#####################################################

import sys
from PIL import Image, ImageDraw, ImageFont

# コマンドライン引数を取得してオプションを判断する
args = sys.argv
argsNum = len( args )

if argsNum != 2 :
    print("コマンドライン引数エラー")
    sys.exit(1);

if len( args[1] ) > 15 :
    print("コマンドライン引数が長すぎます(15文字以下)")
    sys.exit(2);

imageString = args[1] + "には気をつけよう！"
imageStringNum = len( imageString )
image = []

font = ImageFont.truetype("./fonts/Nちはやフォント+.ttf", 27)

# materials内のjpgを読み出して文字を書き込む
# 画像は U-saku_0000.jpg -> U-saku_0043.jpg
for i in range( 0, 44):

    image.insert( i, Image.open("./materials/U-saku_00" + '{0:02d}'.format(i) + ".jpg"))
    draw = ImageDraw.Draw(image[i]);

    draw.text( ( 320-(imageStringNum * 27 / 2), 60), imageString, fill=( 255, 255, 255), font=font)

# gifの作成
# 画像が 15fpsのため duration=66となる
image[0].save( "./gif/" + args[1] + ".gif", save_all=True, append_images=image[1:], optimize=False, duration=66, loop=0)
print("complete!!")
