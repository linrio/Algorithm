#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Lingfeng Lin on Sep. 25, 2017

import xlwt
import os
import os.path
import errno
import re


class txtToscv(object):
    def __init__(self,txt_file_path=None,csv_file_path=None):
        self.a = None
        self.txt_file_path = txt_file_path
        self.csv_file_path = csv_file_path

    def txt_to_scv(self):
        self.a = None
        txt_file = open(self.txt_file_path, "r")
        i = 0
        j = 0
        f_data = xlwt.Workbook()
        data_sheet = f_data.add_sheet('config_perf', cell_overwrite_ok=True)

        arch_params = ['number', 'time', 'counts', 'event']

        # write the table header in excel file
        k = 0
        for param in arch_params:
            data_sheet.write(0, k, param)
            k = k + 1

        for line in txt_file.readlines():
            i+=1
            if i < 4:
                continue
            line.strip().replace(" ", "")

            time = int(float(line[0:16]))
            if line[17:36] != '':
                if '<not supported>' not in line[17:36]:
                    counts = int(line[17:36])
            event = str(line[37:40])
            print(time,counts,event)

            j += 1
            data_sheet.write(j, 0, j)
            data_sheet.write(j, 1, time)
            data_sheet.write(j, 2, counts)
            data_sheet.write(j, 3, event)
            f_data.save('./damo.xls')
            if i > 100:
                break
        return self.a

    def txt_to_scv2(self):
        pattern_file_path = re.compile('ms-(\w*)events')
        event_series = pattern_file_path.findall(self.txt_file_path)[0]
        #print(event_series)
        f_data = xlwt.Workbook()
        data_sheet = f_data.add_sheet('config_perf', cell_overwrite_ok=True)
        arch_params = ['number', 'time', '00', '01', '02', '03', '04', '05']
        arch_params_1 = ['number', 'time', 'SW_INCR', 'L1I_CACHE_REFILL', 'L1I_TLB_REFILL', 'L1D_CACHE_REFILL', 'L1D_CACHE', 'L1D_TLB_REFILL']

        arch_params_2 = ['number', 'time', 'LD_RETIRED', 'ST_RETIRED', 'INST_RETIRED', 'EXC_TAKEN', 'EXC_RETURN', 'CID_WRITE_RETIRED']

        arch_params_3 = ['number', 'time', 'PC_WRITE_RETIRED', 'BR_IMMED_RETIRED', 'BR_RETURN_RETIRED', 'UNALIGNED_LDST_RETIRED', 'BR_MIS_PRED',
                         'CYCLE_COUNT']

        arch_params_4 = ['number', 'time', 'BR_PRED']

        arch_params_5 = ['number', 'time', 'JAVA_BC_EXEC', 'JAVA_SFTBC_EXEC', 'JAVA_BB_EXEC', 'CO_LF_MISS', 'CO_LF_HIT', 'IC_DEP_STALL']

        arch_params_6 = ['number', 'time', 'DC_DEP_STALL', 'STALL_MAIN_TLB', 'STREX_PASS', 'STREX_FAILS', 'DATA_EVICT', 'ISS_NO_DISP']

        arch_params_7 = ['number', 'time', 'ISS_EMPTY', 'INS_RENAME', 'NUMBER_OF_DATA_LINEFILLS', 'NUMBER_OF_PERFETCHER_LINEFILLS',
                         'NUMBER_OF_HITS_IN_PERFETECHED_CACHE_LINES', 'PRD_FN_RET']

        arch_params_8 = ['number', 'time', 'INS_MAIN_EXEC', 'INS_SND_EXEC', 'INS_LSU', 'INS_FP_RR', 'INS_NEON_RR', 'STALL_PLD']

        arch_params_9 = ['number', 'time', 'STALL_WRITE', 'STALL_INS_TLB', 'STALL_DATA_TLB', 'STALL_INS_UTLB', 'STALL_DATA_ULTB', 'STALL_DMB']

        arch_params_10 = ['number', 'time', 'STALL_WRITE', 'CLK_INT_EN', 'CLK_DE_EN', 'NEON_SIMD_CLOCK_ENABLED', 'INSTRUCTION_TLB_ALLOCATION',
                          'DATA_TLB_ALLOCATION']

        arch_params_11 = ['number', 'time', 'INS_ISB', 'INS_DSB', 'INS_DMB', 'EXT_IRQ', 'PLE_CL_REQ_CMP', 'PLE_CL_REQ_SKP']

        arch_params_12 = ['number', 'time', 'PLE_FIFO_FLSH', 'PLE_REQ_COMP', 'PLE_FIFO_OF', 'PLE_REQ_PRG']

        if event_series == 'archi_1':
            arch_params = arch_params_1
        elif event_series == 'archi_2':
            arch_params = arch_params_2
        elif event_series == 'archi_3':
            arch_params = arch_params_3
        elif event_series == 'archi_4':
            arch_params = arch_params_4
        elif event_series == 'archi_5':
            arch_params = arch_params_5
        elif event_series == 'archi_6':
            arch_params = arch_params_6
        elif event_series == 'archi_7':
            arch_params = arch_params_7
        elif event_series == 'archi_8':
            arch_params = arch_params_8
        elif event_series == 'archi_9':
            arch_params = arch_params_9
        elif event_series == 'archi_10':
            arch_params = arch_params_10
        elif event_series == 'archi_11':
            arch_params = arch_params_11
        elif event_series == 'archi_12':
            arch_params = arch_params_12

        #创建csv的表头
        k = 0
        i = 0
        j = 1
        m = 0
        time = None
        counts = None
        event = None
        for param in arch_params:
            data_sheet.write(0, k, param)
            k = k + 1

        #打开txt格式文件，读取，匹配，保存
        txt_file = open(self.txt_file_path, "r")
        for line in txt_file.readlines():
            #过滤前三行与#开头的行
            i += 1
            if i < 4:
                continue
            if '#' in line:
                continue

            line.strip().replace(' ', '')
            if line == '':
                continue

            #正则匹配time, counts, event
            c = str(line[0:16])
            d = str(line[17:36])
            e = str(line[37:39])
            if '.' in c:
                pattern_time = re.compile(r'\d+.\d*')
            else:
                pattern_time = re.compile(r'\d*')
            if '.' in d:
                pattern_counts = re.compile(r'\d*.\d*')
            else:
                pattern_counts = re.compile(r'\d*')
            pattern_event = re.compile(r'\w*')
            try:
                time = pattern_time.findall(c)[0]
                counts = pattern_counts.findall(d)[-3]
                event = pattern_event.findall(e)[0]
                #print(time, counts, event)
            except (ValueError, IndexError):
                print('-----ERROR!--------')
                print(time,counts,event)
                continue
            #print(time, counts, event)
            m+=1
            if m > 6:
                j += 1
                m = 1
            data_sheet.write(j, 0, j)
            if time != '' and counts != '' and event != '':
                data_sheet.write(j, 1, int(float(time)))
            else:
                continue

            if '00' in event or '06' in event or '0C' in event or '12' in event or '40' in event or '61' in event or '67' in event or '70' in event or '81' in event or '8A' in event or '91' in event or 'A3' in event:
                data_sheet.write(j, 2, counts)
            elif '01' in event or '07' in event or '0D' in event or '41' in event or '62' in event or '68' in event or '71' in event or '82' in event or '8B' in event or '92' in event or 'A4' in event:
                data_sheet.write(j, 3, counts)
            elif '02' in event or '08' in event or '0E' in event or '42' in event or '63' in event or '69' in event or '72' in event or '83' in event or '8C' in event or '93' in event or 'A5' in event:
                data_sheet.write(j, 4, counts)
            elif '03' in event or '09' in event or '0F' in event or '50' in event or '64' in event or '6A' in event or '73' in event or '84' in event or '8D' in event or 'A0' in event:
                data_sheet.write(j, 5, counts)
            elif '04' in event or '0A' in event or '10' in event or '51' in event or '65' in event or '6B' in event or '74' in event or '85' in event or '8E' in event or 'A1' in event:
                data_sheet.write(j, 6, counts)
            elif '05' in event or '0B' in event or '11' in event or '60' in event or '66' in event or '6E' in event or '80' in event or '86' in event or '90' in event or 'A2' in event:
                data_sheet.write(j, 7, counts)
            #if i > 10:
            #     break

        f_data.save(self.csv_file_path)
        return self.a

    def read_path(self):
        rootdir = ".\lin_128"  # 指明被遍历的文件夹
        csvdir = ".\csv_128"

        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            # for dirname in dirnames:  # 输出文件夹信息
            #     print("parent is: " + parent)
            #     print("dirname is: " + dirname)
            #     break


            for filename in filenames:  # 输出文件信息
                self.txt_file_path = os.path.join(parent, filename)
                csv_parent = parent.strip().replace(rootdir, csvdir)
                csv_filename = filename.strip().replace(".txt", '.csv')
                self.csv_file_path = str(os.path.join(csv_parent, csv_filename)).strip().replace('\\', '/')
                #print("the full name of the file is: " + self.txt_file_path)  # 输出文件路径信息
                #print("the full name of the file is: " + self.csv_file_path)  # 输出文件路径信息
                self.mkdir_p(csv_parent)
                self.a = self.txt_to_scv2()
                #break
            # break
        return self.a



    def mkdir_p(self, csv_parent):
        #创建文件夹
        try:
            os.makedirs(csv_parent, exist_ok=False)
        except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(csv_parent):
                pass
            else:
                raise

    def GetMiddleStr(self, content, startStr, endStr):
        patternStr = r'%s(.+?)%s' % (startStr, endStr)
        p = re.compile(patternStr, re.IGNORECASE)
        m = re.match(p, content)
        if m:
            return m.group(1)

    def build(self):
        self.a = None
        #self.a = self.txt_to_scv()
        self.a = self.read_path()

if __name__ == '__main__':
    print("-----begin transfer: from txt to excel`s csv-----")
    #txt_file_path = "./lin/DecisionTree-64MB-18slavers-1000ms-archi_1events-1iter-0211185257/slaver3.txt"
    #csv_file_path = "./"
    txttocsv = txtToscv()
    #txttocsv.__init__(txt_file_path, csv_file_path)
    txttocsv.build()
    print("-----end transfer-----")