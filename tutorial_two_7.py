#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tutorial Two 7
# GNU Radio version: 3.7.14.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import threading
import time
from gnuradio import qtgui


class tutorial_two_7(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tutorial Two 7")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tutorial Two 7")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "tutorial_two_7")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.probe_var = probe_var = 0

        ##################################################
        # Blocks
        ##################################################
        self.probe_signal = blocks.probe_signal_f()

        def _probe_var_probe():
            while True:
                val = self.probe_signal.level()
                try:
                    self.set_probe_var(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _probe_var_thread = threading.Thread(target=_probe_var_probe)
        _probe_var_thread.daemon = True
        _probe_var_thread.start()

        self.display = Qt.QTabWidget()
        self.display_widget_0 = Qt.QWidget()
        self.display_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.display_widget_0)
        self.display_grid_layout_0 = Qt.QGridLayout()
        self.display_layout_0.addLayout(self.display_grid_layout_0)
        self.display.addTab(self.display_widget_0, 'Time')
        self.display_widget_1 = Qt.QWidget()
        self.display_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.display_widget_1)
        self.display_grid_layout_1 = Qt.QGridLayout()
        self.display_layout_1.addLayout(self.display_grid_layout_1)
        self.display.addTab(self.display_widget_1, 'Waterfall')
        self.top_grid_layout.addWidget(self.display, 0, 0, 2, 2)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sineee = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10, probe_var, 0)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, 0.0001, 1, 0)
        self.Waterfall = qtgui.waterfall_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.Waterfall.set_update_time(0.10)
        self.Waterfall.enable_grid(False)
        self.Waterfall.enable_axis_labels(True)

        if not True:
          self.Waterfall.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.Waterfall.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Waterfall.set_line_label(i, "Data {0}".format(i))
            else:
                self.Waterfall.set_line_label(i, labels[i])
            self.Waterfall.set_color_map(i, colors[i])
            self.Waterfall.set_line_alpha(i, alphas[i])

        self.Waterfall.set_intensity_range(-140, 10)

        self._Waterfall_win = sip.wrapinstance(self.Waterfall.pyqwidget(), Qt.QWidget)
        self.display_grid_layout_1.addWidget(self._Waterfall_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.display_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.display_grid_layout_1.setColumnStretch(c, 1)
        self.Time = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.Time.set_update_time(0.10)
        self.Time.set_y_axis(-1, 1)

        self.Time.set_y_label('Amplitude', "")

        self.Time.enable_tags(-1, True)
        self.Time.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.Time.enable_autoscale(False)
        self.Time.enable_grid(False)
        self.Time.enable_axis_labels(True)
        self.Time.enable_control_panel(False)
        self.Time.enable_stem_plot(False)

        if not True:
          self.Time.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Time.set_line_label(i, "Data {0}".format(i))
            else:
                self.Time.set_line_label(i, labels[i])
            self.Time.set_line_width(i, widths[i])
            self.Time.set_line_color(i, colors[i])
            self.Time.set_line_style(i, styles[i])
            self.Time.set_line_marker(i, markers[i])
            self.Time.set_line_alpha(i, alphas[i])

        self._Time_win = sip.wrapinstance(self.Time.pyqwidget(), Qt.QWidget)
        self.display_grid_layout_0.addWidget(self._Time_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.display_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.display_grid_layout_0.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.probe_signal, 0))
        self.connect((self.sineee, 0), (self.Time, 0))
        self.connect((self.sineee, 0), (self.Waterfall, 0))
        self.connect((self.sineee, 0), (self.audio_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tutorial_two_7")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.sineee.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.Waterfall.set_frequency_range(0, self.samp_rate)
        self.Time.set_samp_rate(self.samp_rate)

    def get_probe_var(self):
        return self.probe_var

    def set_probe_var(self, probe_var):
        self.probe_var = probe_var
        self.sineee.set_amplitude(self.probe_var)


def main(top_block_cls=tutorial_two_7, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
