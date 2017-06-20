#!/bin/python
# -*- coding: utf-8 -*-


# 檔案結構：
#
# packageA (資料夾)
#   ---(__init__.py)
#   ---moduleA(moduleA.py)
#        ---TestCaseA (class)
#   ---moduleB(moduleB.py)
#        ---TestCaseB (class)
#   ---moduleC(moduleC.py)
#        ---TestCaseC (class)
# 
# 因為有了 __init__.py 這個 packageA 資料夾就會形成，python 的 package
# 就可以使用 import packageA 這種東西 (要成為package 必須要在資料夾內有 __init__.py 這檔案)
# 參考: https://docs.python.org/2/tutorial/modules.html#packages
# 
# 進階閱讀 __all__
#
#
# ---***  Unit Test ***---
# 基本參考資料： https://docs.python.org/2/library/unittest.html
# 基本用法： 1. 因為moduleA/B/C 每隻都有自帶 if __name__=='__main__' 以下簡稱 main 
#               所以可以直接用 python 執行 (不會產生 pyc)
#            2. 如果沒有 main 可以使用 python -m unittest ${moudle} 執行 (會產生.pyc 因為 python 是引用他的module)
#               e.g. 直接測試 :                      python -m unittest packageA.moduleA
#               e.g. 直接測試 module(可多個):        cd packageA 之後 python -m unittest moduleA moduleB
#               e.g. 針對TestCase (class):           cd packageA 之後 python -n unittest moduleA.TestCaseA
#               e.g. 針對TestCase 中的函式:          cd packageA 之後 python -n unittest moduleA.TestCaseA.test_case_A_1
#  *** NOTE *** 不能直接測試 package 本身 
#               e.g. 直接測試 : python -m unittest packageA
#               會得到空的測試資料喔(Ran 0 tests in 0.000s)！！(因為python -m unittest 的測試是檢查
#               你的.py 中是否有 class XXX(unittest.TestCase) ，而unittest.TestCase 檢查機制是判斷這 class 中是否有 test 開頭的關鍵字來決定tests)。
#               可以比較 moduleA/B/C.py 的程式內容及執行結果。  
#               參考資料: https://docs.python.org/2/library/unittest.html#command-line-interface
#
# 進階用法：測試資料夾內的**所有** unittest.py
# 參考：https://docs.python.org/2/library/unittest.html#test-discovery
# 用法： 1. cd 到資料夾 e.g. cd packageB 之後 python -m unittest discover
#           python -m unittest discover $資料夾路徑 
#           預設會搜尋 test 關鍵字開頭的.py 檔案 
#           packageA 這個 directory 因為沒有 test 開頭，所以會找不到喔。
#
#        2. (好用）python -m unittest discover -v -s ${資料夾} -p "*_test.py" 
#            參數 -v 詳細地列出每個執行過程
#                 -s 指定資料夾
#                 -p 指定要被測試的檔案樣式  e.g. "test_*.py" 或是 "*_test.py" 都是很常見的習慣命名
#
#        因為畢竟是 unittest
#        而且通常是一個 project 架構是如此
#        project
#           ---packageA
#              ---moduleA(XXX.py)
#                 ---classA
#           ---test
#              ---unittest
#                 ---test_xxx.py
#
#
#
#  待續:
#  test_suite 及 load_test 和 test result 蒐集
