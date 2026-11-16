from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import System32
import os

def Auto(path): return os.path.dirname(System32.file.Self()) + '\\' + path

window_config = {
    'window_icon': Auto(r'icon\Windows Dynamic Island.png'),
    'window_title': "入门",
    'width': 1000,
    'height': 650,
}

welcome_Label_config = {
    'start_y': 100,
    'start_animation': True,
    'start_animation_speed': 2.0,
    'text': '欢迎',
    'x': 200,
    'y': 100,
    'font_size': 48,
    'duration': 1000,
}

use_Label_config = {
    'end_x': 400,
    'start_animation': True,
    'start_animation_speed': 2.0,
    'text': '使用',
    'y': 400,
    'font_size': 64,
    'duration': 1000,
}

Title_Label_config = {
    'end_x': 75,
    'start_animation': True,
    'start_animation_speed': 2.0,
    'text': 'Windows Dynamic Island',
    'y': 200,
    'font_size': 72,
    'duration': 1000,
}

topic_Label_config = {
    'text': '请选择主题',
    'end_x': 100,
    'start_animation': True,
    'start_animation_speed': 2.0,
    'y': 100,
    'font_size': 48,
    'duration': 1000,
    'topics':['浅色', 'light topics', 
              '深色', 'black topcs',
              '简单', 'simpleness', 
              '极简', 'Minimalism', 
              '系统信息', 'System Info', 
              '时间', 'timer', 
        ]
}

data = {
    'topic':None
}

# ===================== 窗口初始化 =====================
app = QApplication(sys.argv)
root = QWidget()
root.resize(window_config['width'], window_config['height'])
root.setWindowTitle(window_config['window_title'])
if os.path.exists(window_config['window_icon']):
    root.setWindowIcon(QIcon(QPixmap(window_config['window_icon'])))
root.show()

# 共用动画参数
ease_curve = QEasingCurve(QEasingCurve.Type.OutQuad)
padding_w = 40
padding_h = 20
fade_duration = 1200

# ==================================================
# 【第一出场：欢迎标签】
# ==================================================
welcome_Label = QLabel(text=welcome_Label_config['text'], parent=root)
welcome_Label.setStyleSheet(f"font-size:{welcome_Label_config['font_size']}px;")
hint_size = welcome_Label.sizeHint()
auto_w = hint_size.width() + padding_w
auto_h = hint_size.height() + padding_h
start_y_welcome = -auto_h
end_y_welcome = welcome_Label_config['start_y']
welcome_Label.setGeometry(welcome_Label_config['x'], start_y_welcome, auto_w, auto_h)
welcome_Label.show()

# 欢迎滑动动画
anim_welcome = QPropertyAnimation(welcome_Label, b"pos")
anim_welcome.setDuration(welcome_Label_config['duration'])
anim_welcome.setEasingCurve(ease_curve)
anim_welcome.setStartValue(QPoint(welcome_Label_config['x'], start_y_welcome))
anim_welcome.setEndValue(QPoint(welcome_Label_config['x'], end_y_welcome))

# 欢迎透明度
opacity_welcome = QGraphicsOpacityEffect()
welcome_Label.setGraphicsEffect(opacity_welcome)
opacity_welcome.setOpacity(1.0)

# ==================================================
# 【第二出场：使用标签】
# ==================================================
use_Label = QLabel(text=use_Label_config['text'], parent=root)
use_Label.setStyleSheet(f"font-size:{use_Label_config['font_size']}px;")
hint_size_use = use_Label.sizeHint()
auto_w_use = hint_size_use.width() + padding_w
auto_h_use = hint_size_use.height() + padding_h
start_x_use = -auto_w_use
end_x_use = use_Label_config['end_x']
use_Label.setGeometry(start_x_use, use_Label_config['y'], auto_w_use, auto_h_use)
use_Label.show()

# 使用滑动动画
anim_use = QPropertyAnimation(use_Label, b"pos")
anim_use.setDuration(use_Label_config['duration'])
anim_use.setEasingCurve(ease_curve)
anim_use.setStartValue(QPoint(start_x_use, use_Label_config['y']))
anim_use.setEndValue(QPoint(end_x_use, use_Label_config['y']))

# 使用透明度
opacity_use = QGraphicsOpacityEffect()
use_Label.setGraphicsEffect(opacity_use)
opacity_use.setOpacity(1.0)

# ==================================================
# 【第三出场：标题标签】
# ==================================================
Title_Label = QLabel(text=Title_Label_config['text'], parent=root)
Title_Label.setStyleSheet(f"font-size:{Title_Label_config['font_size']}px;")
hint_size_title = Title_Label.sizeHint()
auto_w_title = hint_size_title.width() + padding_w
auto_h_title = hint_size_title.height() + padding_h
start_x_title = window_config['width']
end_x_title = Title_Label_config['end_x']
Title_Label.setGeometry(start_x_title, Title_Label_config['y'], auto_w_title, auto_h_title)
Title_Label.show()

# 标题滑动动画
anim_title = QPropertyAnimation(Title_Label, b"pos")
anim_title.setDuration(Title_Label_config['duration'])
anim_title.setEasingCurve(ease_curve)
anim_title.setStartValue(QPoint(start_x_title, Title_Label_config['y']))
anim_title.setEndValue(QPoint(end_x_title, Title_Label_config['y']))

# 标题透明度
opacity_title = QGraphicsOpacityEffect()
Title_Label.setGraphicsEffect(opacity_title)
opacity_title.setOpacity(1.0)

# ==================================================
# 旧三个标签的淡出动画组
# ==================================================
anim_fade_welcome = QPropertyAnimation(opacity_welcome, b"opacity")
anim_fade_use = QPropertyAnimation(opacity_use, b"opacity")
anim_fade_title = QPropertyAnimation(opacity_title, b"opacity")

for fade_anim in [anim_fade_welcome, anim_fade_use, anim_fade_title]:
    fade_anim.setDuration(fade_duration)
    fade_anim.setStartValue(1.0)
    fade_anim.setEndValue(0.0)
    fade_anim.setEasingCurve(QEasingCurve.Type.OutQuad)

# ==================================================
# 【第四出场：Topic标签 请选择主题】
# ==================================================
topic_Label = QLabel(text=topic_Label_config['text'], parent=root)
topic_Label.setStyleSheet(f"font-size:{topic_Label_config['font_size']}px;")
hint_size_topic = topic_Label.sizeHint()
auto_w_topic = hint_size_topic.width() + padding_w
auto_h_topic = hint_size_topic.height() + padding_h
start_x_topic = -auto_w_topic
end_x_topic = topic_Label_config['end_x']
topic_y = topic_Label_config['y']
topic_Label.setGeometry(start_x_topic, topic_y, auto_w_topic, auto_h_topic)
topic_Label.hide()

# topic透明度
opacity_topic = QGraphicsOpacityEffect()
topic_Label.setGraphicsEffect(opacity_topic)
opacity_topic.setOpacity(0.0)

# topic滑动动画
anim_topic_slide = QPropertyAnimation(topic_Label, b"pos")
anim_topic_slide.setDuration(topic_Label_config['duration'])
anim_topic_slide.setEasingCurve(ease_curve)
anim_topic_slide.setStartValue(QPoint(start_x_topic, topic_y))
anim_topic_slide.setEndValue(QPoint(end_x_topic, topic_y))

# topic淡入动画
anim_topic_fadein = QPropertyAnimation(opacity_topic, b"opacity")
anim_topic_fadein.setDuration(topic_Label_config['duration'])
anim_topic_fadein.setEasingCurve(ease_curve)
anim_topic_fadein.setStartValue(0.0)
anim_topic_fadein.setEndValue(1.0)

def start_topic_anim():
    topic_Label.show()
    anim_topic_slide.start()
    anim_topic_fadein.start()

# 旧标签淡出完成回调：销毁旧标签，启动topic
def on_fade_finished():
    welcome_Label.deleteLater()
    use_Label.deleteLater()
    Title_Label.deleteLater()
    start_topic_anim()

# 全部滑动动画跑完，等待3s，执行淡出
def after_all_slide():
    wait_tool.wait(3000, lambda: (
        anim_fade_welcome.start(),
        anim_fade_use.start(),
        anim_fade_title.start()
    ))

class WaitTimer(QTimer):
    def __init__(self):
        super().__init__()
        self.callback = None
        self.timeout.connect(self._on_timeout)
    def wait(self, ms: int, callback):
        self.stop()
        self.callback = callback
        self.start(ms)
    def _on_timeout(self):
        self.stop()
        if self.callback is not None:
            self.callback()

wait_tool = WaitTimer()
anim_welcome.finished.connect(anim_use.start)
anim_use.finished.connect(anim_title.start)
anim_title.finished.connect(after_all_slide)
anim_fade_title.finished.connect(on_fade_finished)

wait_tool.wait(1000, lambda: anim_welcome.start())

topic = QComboBox(root)
topic.setGeometry(100, 180, 120, 40)
topic.addItems(topic_Label_config['topics'])
topic.hide()

topic_combo_opacity = QGraphicsOpacityEffect()
topic.setGraphicsEffect(topic_combo_opacity)
topic_combo_opacity.setOpacity(0.0)

anim_combo_fade = QPropertyAnimation(topic_combo_opacity, b"opacity")
anim_combo_fade.setDuration(800)
anim_combo_fade.setStartValue(0.0)
anim_combo_fade.setEndValue(1.0)
anim_combo_fade.setEasingCurve(ease_curve)

def on_topic_selected(): data['topic'] = topic.currentText()

topic.currentIndexChanged.connect(on_topic_selected)

def show_topic_combo():
    topic.show()
    anim_combo_fade.start()

anim_topic_slide.finished.connect(show_topic_combo)

sys.exit(app.exec())