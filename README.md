# 自然场景图片的文字区域定位及去水印 v0.1

Suppport JPG, PNG

## Src
./src/demark

## Install
pip install -r requirements.txt

## Usage
python remove_text.py data/1.jpg data/1_result.jpg           

Params:
- data/1.jpg: souce image
- data/1_result.jpg: result file name

## V0.2 reference:
http://wap.cnki.net/touch/web/Dissertation/Article/10701-1011075451.nh.html
http://cea.ceaj.org/CN/article/downloadArticleFile.do?attachType=PDF&id=22109

SUSAN角点检测算法：
https://github.com/rajatjain3571/Susan-Corner-Detection
