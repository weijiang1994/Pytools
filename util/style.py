"""
@Time    : 2020/1/20 13:35
@Author  : weijiang
@Site    : 
@File    : style.py
@Software: PyCharm
"""
LEFT_WIDGET_STYLE = "QListWidget{" \
                    "background:#383838;" \
                    "color:#000000;" \
                    "font: 14pt Arial;"\
                    "border:0px solid gray;" \
                    "padding:0px;}" \
                    \
                    "QListWidget::item{" \
                    "width:94px;" \
                    "height:45px;" \
                    "border:0px solid gray;" \
                    "padding-left:24px;}" \
                    \
                    "QListWidget::item:selected:active{" \
                    "background:rgb(40, 40, 40);color:#ffffff;" \
                    "border-width:-1;}" \
                    \
                    "QListWidget::item:selected{" \
                    "background:rgb(40, 40, 40);color:#ffffff;}"

CAL_PUSHBUTTON_STYLE = "QPushButton{background-color:#3c3c3c;border-radius:3px;border:1px;color:white;}" \
                       "QPushButton:hover{" \
                       "background-color:#2B2B2B;" \
                       "color:#FFFFFF}" \
                       "QPushButton:pressed{background-color:#3C3F41}"

VERTICAL_SCROLL_BAR_STYLE = "QScrollBar{background-color:#FFF; width:10px;}" \
                            "QScrollBar::handle{background-color:rgb(29, 29, 29); border:2px solid transparent; border-radius:5px;}" \
                            "QScrollBar::handle:hover{background-color:rgb(139, 139, 139);}" \
                            "QScrollBar::sub-line{background:transparent;}" \
                            "QScrollBar::add-line{background:transparent;}"

TOP_WIDGET_STYLE = "QListWidget{" \
                   "background:#383838;" \
                   "color:#000000;" \
                   "font: 14pt Arial;"\
                   "border:0px solid gray;" \
                   "padding:0px;}" \
 \
                   "QListWidget::item{" \
                   "width:160px;" \
                   "height:38px;" \
                   "border:0px solid gray;" \
                   "padding-left:24px;}" \
 \
                   "QListWidget::item:selected:active{" \
                   "background:#2B2B2B;color:#FFFFFF;" \
                   "border-width:-1;" \
                   "border-bottom: 5px solid #F9C138;}" \
 \
                   "QListWidget::item:selected{" \
                   "background:#2B2B2B;color:#FFFFFF;" \
                   "border-bottom: 5px solid #F9C138;}"