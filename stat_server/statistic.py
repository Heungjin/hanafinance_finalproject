# -*- coding: ms949 -*-

import pymysql
import threading
from time import sleep,ctime
from datetime import datetime


def create_customer_info_table():
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE customer_info (
                cus_num int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                cus_age int(4),
                cus_sex int(4),
                repayment int(4),
                repayment_money Double,
                cus_salary Double,
                cus_loan Double,
                leasing_mortgage Double,
                month_loan_period int(4),
                bank_id int(4),
                input_date datetime default now()
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
        conn.commit()
    except:
        print 'customer_info table already existed'
    finally:
        conn.close()
        
def create_loan_goods_table():
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE loan_goods (
                loan_good_num int(4) primary key,
                loan_good_name varchar(50),
                loan_bank_id int(4),
                avg_int_rat Double,
                money_credit_line Double,
                rate_credit_line Double,
                salary_credit_line Double,
                month_loan_period_line int(11),
                loan_repayment int(11),
                loan_url varchar(255),
				loan_img varchar(50),
                num_recommend int(11),
				chatbot_img varchar(50),
				chatbot_description varchar(255),
				chat_recommend int(11)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
        conn.commit()
    except:
        print 'loan_goods table already existed'
    finally:
        conn.close()
        
def create_tb_calc_table():
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE tb_calc (
                calc_num int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                cus_num int(11),
				loan_good_num int,
                loan_good_name varchar(255),
                like_loan int(4)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
        conn.commit()
    except:
        print 'tb_calc table already existed'
    finally:
        conn.close()

def create_tb_calc2_table():
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE tb_calc2 (
                cus_num int(11),
                loan_good_num int(4),
                loan_good_name varchar(255),
                select_date datetime default now()
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
        conn.commit()
    except:
        print 'tb_calc2 table already existed'
    finally:
        conn.close()

def create_statistics_table():
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:          
            sql = '''
            CREATE TABLE statistic_loan_amount (
               type varchar(255),
               m0_3 int(11),
               m3_5 int(11),
               m5_7 int(11),
               m7_10 int(11),
               m10_15 int(11),
               m15_20 int(11),
               m20_0 int(11)             
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('total'))
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_bank'))
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('repayment_0'))
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('repayment_1'))
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_y'))
            
            sql = '''
            INSERT INTO statistic_loan_amount (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_m'))
            
            
        conn.commit()        
    except:
        print 'statistic_loan_amount table already existed'
    finally:
        conn.close()
    
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE statistic_age (
               type varchar(255),
               loan_good_num int(11),
               m0_20 int(11) default 0,
               m20_30 int(11) default 0,
               m30_40 int(11) default 0,
               m40_50 int(11) default 0,
               m50_60 int(11) default 0,
               m60_0 int(11) default 0
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('total'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_bank'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('repayment_0'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('repayment_1'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_y'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_m'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('one'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('two'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('three'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('four'))
            
            sql = '''
            INSERT INTO statistic_age (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('five'))
            
        conn.commit()        
    except:
        print 'statistic_age table already existed'
    finally:
        conn.close()
    
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE statistic_salary (
               type varchar(255),
               m0_2 int(11),
               m2_3 int(11),
               m3_4 int(11),
               m4_5 int(11),
               m5_7 int(11),
               m7_10 int(11),
               m10_0 int(11)         
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
            
            sql = '''
            INSERT INTO statistic_salary (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('total'))
                        
            sql = '''
            INSERT INTO statistic_salary (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_y'))
            
            sql = '''
            INSERT INTO statistic_salary (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('prefer_m'))
            
        conn.commit()        
    except:
        print 'statistic_salary table already existed'
    finally:
        conn.close()
        
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = '''
            CREATE TABLE statistic_list (
               type varchar(255),
               m1_loan_good_num int(4),
               m1_num int(11),
               m2_loan_good_num int(4),
               m2_num int(11),
               m3_loan_good_num int(4),
               m3_num int(11),
			   total int(11)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
            cursor.execute(sql)
            
            sql = '''
            INSERT INTO statistic_list (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('old_list'))
            
            sql = '''
            INSERT INTO statistic_list (type)
            VALUES (%s)
            '''
            cursor.execute(sql,('new_list'))
            
        conn.commit()        
    except:
        print 'statistic_list table already existed'
    finally:
        conn.close()
        
   
def init():

    create_customer_info_table()
    create_loan_goods_table()
    create_statistics_table()
    create_tb_calc_table()
    create_tb_calc2_table()
    
##############     loan_amount     ########################################################
        
def loan_amount_total(num_s, num_l):
    print 'loan_amount_total'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT count(*) FROM customer_info WHERE cus_loan >= %s and cus_loan < %s'
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = 0
            for data in result:
                cnt = data.get('count(*)')
                
    finally:
        conn.close()
   
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 20):
                num_s = 20
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_loan_amount SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt,'total'))
        conn.commit()              
    finally:
        conn.close()
        
def loan_amount_prefer_bank(num_s, num_l):
    print 'loan_amount_prefer_bank'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
            SELECT bank_id
            FROM(   SELECT bank_id, count(bank_id) cnt 
                    FROM customer_info 
                    WHERE cus_loan >= %s and cus_loan < %s 
                    group by bank_id) bank, 
                (   SELECT max(b.cnt2) max_cnt
                    FROM(   SELECT bank_id, count(bank_id) cnt2
                            FROM customer_info 
                            WHERE cus_loan >= %s and cus_loan < %s
                            group by bank_id) b) m
            WHERE bank.cnt = m.max_cnt
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000, num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = 0
            for data in result:
                cnt = data.get('bank_id')
                
    finally:
        conn.close()
        
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 20):
                num_s = 20
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_loan_amount SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt,'prefer_bank'))
        conn.commit()              
    finally:
        conn.close()
        
def loan_amount_repayment(num_s, num_l):
    print 'loan_amount_repayment'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
            SELECT repayment, count(repayment) cnt 
            FROM customer_info 
            WHERE cus_loan >= %s and cus_loan < %s 
            group by repayment
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = [0,0]
            for data in result:
                cnt[data.get('repayment')] = data.get('cnt')
    finally:
        conn.close()
        
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 20):
                num_s = 20
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_loan_amount SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'repayment_0'))
            cursor.execute(sql,(cnt[1],'repayment_1'))
        conn.commit()
    finally:
        conn.close()
        

def loan_amount_prefer_loan(num_s, num_l):
    print 'loan_amount_prefer_loan'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
                SELECT cal.like_loan loan, count(cal.like_loan) cnt
                FROM customer_info cus
                JOIN tb_calc cal ON(cus.cus_num = cal.cus_num)
                WHERE cus.cus_loan >= %s and cus.cus_loan < %s
                group by cal.like_loan;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = [0,0]
            for data in result:
                cnt[data.get('loan')] = data.get('cnt')
    finally:
        conn.close()

    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 20):
                num_s = 20
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_loan_amount SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'prefer_y'))
            cursor.execute(sql,(cnt[1],'prefer_m'))
        conn.commit()
    finally:
        conn.close()
######################################################################

##############     age     ########################################################
        
def age_total(num_s, num_l):
    print 'age_total'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT count(*) FROM customer_info WHERE cus_age >= %s and cus_age < %s'
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s, num_l))
            result = cursor.fetchall()
            cnt = 0
            for data in result:
                cnt = data.get('count(*)')
                
    finally:
        conn.close()
   
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 60):
                num_s = 60
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_age SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt,'total'))
        conn.commit()              
    finally:
        conn.close()
        
def age_prefer_bank(num_s, num_l):
    print 'age_prefer_bank'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
            SELECT bank_id
            FROM(   SELECT bank_id, count(bank_id) cnt 
                    FROM customer_info 
                    WHERE cus_age >= %s and cus_age < %s 
                    group by bank_id) bank, 
                (   SELECT max(b.cnt2) max_cnt
                    FROM(   SELECT bank_id, count(bank_id) cnt2
                            FROM customer_info 
                            WHERE cus_age >= %s and cus_age < %s
                            group by bank_id) b) m
            WHERE bank.cnt = m.max_cnt
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s, num_l, num_s, num_l))
            result = cursor.fetchall()
            cnt = 0
            for data in result:
                cnt = data.get('bank_id')
                
    finally:
        conn.close()
        
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 60):
                num_s = 60
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_age SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt,'prefer_bank'))
        conn.commit()              
    finally:
        conn.close()
        
def age_repayment(num_s, num_l):
    print 'age_repayment'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
            SELECT repayment, count(repayment) cnt 
            FROM customer_info 
            WHERE cus_age >= %s and cus_age < %s 
            group by repayment
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s, num_l))
            result = cursor.fetchall()
            cnt = [0,0]
            for data in result:
                cnt[data.get('repayment')] = data.get('cnt')
    finally:
        conn.close()
        
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 60):
                num_s = 60
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_age SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'repayment_0'))
            cursor.execute(sql,(cnt[1],'repayment_1'))
        conn.commit()
    finally:
        conn.close()
        

def age_prefer_loan(num_s, num_l):
    print 'age_prefer_loan'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
                SELECT cal.like_loan loan, count(cal.like_loan) cnt
                FROM customer_info cus
                JOIN tb_calc cal ON(cus.cus_num = cal.cus_num)
                WHERE cus.cus_age >= %s and cus.cus_age < %s
                group by cal.like_loan;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s, num_l))
            result = cursor.fetchall()
            cnt = [0,0]
            for data in result:
                cnt[data.get('loan')] = data.get('cnt')
    finally:
        conn.close()

    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 60):
                num_s = 60
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_age SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'prefer_y'))
            cursor.execute(sql,(cnt[1],'prefer_m'))
        conn.commit()
    finally:
        conn.close()
        
        
def age_list():
    print 'age_list'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
                select loan_good.loan_good_num, loan_good.cnt
                from (select loan_good_num, count(loan_good_num) cnt
                    from tb_calc2
                    group by loan_good_num) loan_good
                order by loan_good.cnt desc limit 5;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            cnt_count = 0
            cnt = [0,0,0,0,0]
            for data in result:
                cnt[cnt_count] = data.get('loan_good_num')
                cnt_count = cnt_count + 1
                
                
                
            sql = 'UPDATE statistic_age SET loan_good_num = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'one'))
            cursor.execute(sql,(cnt[1],'two'))
            cursor.execute(sql,(cnt[2],'three'))
            cursor.execute(sql,(cnt[3],'four'))
            cursor.execute(sql,(cnt[4],'five'))
            conn.commit()
            
            ###########################################################################################################################
            
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 0 and info.cus_age < 20) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            one = [0,0,0,0,0]
            one_num = [0,0,0,0,0]
            one_cnt = 0
            for data in result:
                one[one_cnt] = data.get('cnt')
                one_num[one_cnt] = data.get('loan_good_num')
                one_cnt = one_cnt +1
            
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 20 and info.cus_age < 30) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            two = [0,0,0,0,0]
            two_num = [0,0,0,0,0]
            two_cnt = 0
            for data in result:
                two[two_cnt] = data.get('cnt')
                two_num[two_cnt] = data.get('loan_good_num')
                two_cnt = two_cnt +1
                
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 30 and info.cus_age < 40) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            three = [0,0,0,0,0]
            three_num = [0,0,0,0,0]
            three_cnt = 0
            for data in result:
                three[three_cnt] = data.get('cnt')
                three_num[three_cnt] = data.get('loan_good_num')
                three_cnt = three_cnt +1
                
                
            
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 40 and info.cus_age < 50) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            four = [0,0,0,0,0]
            four_num = [0,0,0,0,0]
            four_cnt = 0
            for data in result:
                four[four_cnt] = data.get('cnt')
                four_num[four_cnt] = data.get('loan_good_num')
                four_cnt = four_cnt +1
                
                
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 50 and info.cus_age < 60) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            five = [0,0,0,0,0]
            five_num = [0,0,0,0,0]
            five_cnt = 0
            for data in result:
                five[five_cnt] = data.get('cnt')
                five_num[five_cnt] = data.get('loan_good_num')
                five_cnt = five_cnt +1
                
                
                
            sql = '''
                select b.cnt, b.loan_good_num
                from (select count(*) cnt, a.loan_good_num
                        from (select cal.cus_num, cal.loan_good_num, cal.loan_good_name, info.cus_age
                                from tb_calc2 cal
                                join customer_info info on(cal.cus_num = info.cus_num)
                                where info.cus_age >= 60 and info.cus_age < 100) a
                        group by a.loan_good_num) b,
                        (select loan_good.loan_good_num, loan_good.cnt
                            from (select loan_good_num, count(loan_good_num) cnt
                                from tb_calc2
                                group by loan_good_num) loan_good
                            order by loan_good.cnt desc limit 5) c
                where b.loan_good_num in(c.loan_good_num)
                order by b.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            six = [0,0,0,0,0]
            six_num = [0,0,0,0,0]
            six_cnt = 0
            for data in result:
                six[six_cnt] = data.get('cnt')
                six_num[six_cnt] = data.get('loan_good_num')
                six_cnt = six_cnt +1
                
                
                
            ##################################################################################################
            m0_20 = 'm0_20'
            sql = 'UPDATE statistic_age SET '+m0_20+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(one[0],one_num[0]))
            cursor.execute(sql,(one[1],one_num[1]))
            cursor.execute(sql,(one[2],one_num[2]))
            cursor.execute(sql,(one[3],one_num[3]))
            cursor.execute(sql,(one[4],one_num[4]))
            conn.commit()
            
            m20_30 = 'm20_30'
            sql = 'UPDATE statistic_age SET '+m20_30+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(two[0],two_num[0]))
            cursor.execute(sql,(two[1],two_num[1]))
            cursor.execute(sql,(two[2],two_num[2]))
            cursor.execute(sql,(two[3],two_num[3]))
            cursor.execute(sql,(two[4],two_num[4]))
            conn.commit()
            
            m30_40 = 'm30_40'
            sql = 'UPDATE statistic_age SET '+m30_40+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(three[0],three_num[0]))
            cursor.execute(sql,(three[1],three_num[1]))
            cursor.execute(sql,(three[2],three_num[2]))
            cursor.execute(sql,(three[3],three_num[3]))
            cursor.execute(sql,(three[4],three_num[4]))
            conn.commit()
            
            m40_50 = 'm40_50'
            sql = 'UPDATE statistic_age SET '+m40_50+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(four[0],four_num[0]))
            cursor.execute(sql,(four[1],four_num[1]))
            cursor.execute(sql,(four[2],four_num[2]))
            cursor.execute(sql,(four[3],four_num[3]))
            cursor.execute(sql,(four[4],four_num[4]))
            conn.commit()
            
            m50_60 = 'm50_60'
            sql = 'UPDATE statistic_age SET '+m50_60+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(five[0],five_num[0]))
            cursor.execute(sql,(five[1],five_num[1]))
            cursor.execute(sql,(five[2],five_num[2]))
            cursor.execute(sql,(five[3],five_num[3]))
            cursor.execute(sql,(five[4],five_num[4]))
            conn.commit()
            
            m60_0 = 'm60_0'
            sql = 'UPDATE statistic_age SET '+m60_0+' = %s WHERE loan_good_num = %s;'
            cursor.execute(sql,(six[0],six_num[0]))
            cursor.execute(sql,(six[1],six_num[1]))
            cursor.execute(sql,(six[2],six_num[2]))
            cursor.execute(sql,(six[3],six_num[3]))
            cursor.execute(sql,(six[4],six_num[4]))
            conn.commit()
    finally:
        conn.close()

######################################################################


##############     salary     ########################################################
        
def salary_total(num_s, num_l):
    print 'salary_total'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT count(*) FROM customer_info WHERE cus_salary >= %s and cus_salary < %s'
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = 0
            for data in result:
                cnt = data.get('count(*)')
                
    finally:
        conn.close()
   
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 10):
                num_s = 10
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_salary SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt,'total'))
        conn.commit()              
    finally:
        conn.close()        

def salary_prefer_loan(num_s, num_l):
    print 'salary_prefer_loan'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
                SELECT cal.like_loan loan, count(cal.like_loan) cnt
                FROM customer_info cus
                JOIN tb_calc cal ON(cus.cus_num = cal.cus_num)
                WHERE cus.cus_salary >= %s and cus.cus_salary < %s
                group by cal.like_loan;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(num_s*10000000, num_l*10000000))
            result = cursor.fetchall()
            cnt = [0,0]
            for data in result:
                cnt[data.get('loan')] = data.get('cnt')
    finally:
        conn.close()

    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            
            if(num_s == 0):
                num_s = 0
                
            if(num_s >= 10):
                num_s = 10
                num_l = 0

            temp = 'm'+str(num_s) + '_' + str(num_l)
            
            sql = 'UPDATE statistic_salary SET '+temp+' = %s WHERE type = %s'
            cursor.execute(sql,(cnt[0],'prefer_y'))
            cursor.execute(sql,(cnt[1],'prefer_m'))
        conn.commit()
    finally:
        conn.close()
######################################################################

########################## list ############################################

def total_list():
    print 'total_list'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')

    try:
        with conn.cursor() as cursor:
            sql = '''
            select loan_good.loan_good_num loan_good_num, loan_good.cnt num_recommend
            from (select loan_good_num, count(loan_good_num) cnt
            from tb_calc2
            group by loan_good_num) loan_good
            order by loan_good.cnt desc;
            '''
            #sql = '''
            #select loan_good_num, num_recommend
            #from loan_goods
            #order by num_recommend desc;
            #'''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            print result

            name_num = []
            cnt = []
            k = 0
            total = 0
			
            for data in result:
                name_num.append(data.get('loan_good_num'))
                cnt.append(data.get('num_recommend'))
                total = total + cnt[k]
                k = k + 1
            print name_num
    finally:
        conn.close()

    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE statistic_list SET m1_loan_good_num = %s, m1_num = %s, m2_loan_good_num = %s, m2_num = %s, m3_loan_good_num = %s, m3_num = %s, total = %s WHERE type = %s'
            cursor.execute(sql,(name_num[0], cnt[0], name_num[1], cnt[1], name_num[2], cnt[2], total, 'old_list'))
        conn.commit()
    finally:
        conn.close()

def recent_list():
    print 'recent_list'
    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8') 
    try:
        with conn.cursor() as cursor:
            sql = '''
            select loan_good.loan_good_num, loan_good.cnt
            from (select loan_good_num, count(loan_good_num) cnt
                from tb_calc2
                where select_date > date_add(now(), interval -6 month)
                group by loan_good_num) loan_good
            order by loan_good.cnt desc;
            '''
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            print result
            name_num = []
            cnt = []
            k = 0
            total = 0
            for data in result:
                name_num.append(data.get('loan_good_num'))
                cnt.append(data.get('cnt'))
                total = total + cnt[k]
                k = k + 1
            print name_num
    finally:
        conn.close()

    conn = pymysql.connect(host='hana-finance.c7qldhnfrqvy.ap-northeast-2.rds.amazonaws.com', user='admin', password='wjsgmdwls', db='hanaproject', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE statistic_list SET m1_loan_good_num = %s, m1_num = %s, m2_loan_good_num = %s, m2_num = %s, m3_loan_good_num = %s, m3_num = %s, total = %s WHERE type = %s'
            cursor.execute(sql,(name_num[0], cnt[0], name_num[1], cnt[1], name_num[2], cnt[2],total, 'new_list'))
        conn.commit()
    finally:
        conn.close()


class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        print 'statistics start'
        
        ##################### loan_amount ############################
        loan_amount_total(0,3)
        loan_amount_total(3,5)
        loan_amount_total(5,7)
        loan_amount_total(7,10)
        loan_amount_total(10,15)
        loan_amount_total(15,20)
        loan_amount_total(20,0)
        
        loan_amount_prefer_bank(0,3)
        loan_amount_prefer_bank(3,5)
        loan_amount_prefer_bank(5,7)
        loan_amount_prefer_bank(7,10)
        loan_amount_prefer_bank(10,15)
        loan_amount_prefer_bank(15,20)
        loan_amount_prefer_bank(20,0)
        
        loan_amount_repayment(0,3)
        loan_amount_repayment(3,5)
        loan_amount_repayment(5,7)
        loan_amount_repayment(7,10)
        loan_amount_repayment(10,15)
        loan_amount_repayment(15,20)
        loan_amount_repayment(20,0)
        
        loan_amount_prefer_loan(0,3)
        loan_amount_prefer_loan(3,5)
        loan_amount_prefer_loan(5,7)
        loan_amount_prefer_loan(7,10)
        loan_amount_prefer_loan(10,15)
        loan_amount_prefer_loan(15,20)
        loan_amount_prefer_loan(20,0)
        
        #################### age               #####################
        age_total(0,20)
        age_total(20,30)
        age_total(30,40)
        age_total(40,50)
        age_total(50,60)
        age_total(60,0)
        
        age_prefer_bank(0,20)
        age_prefer_bank(20,30)
        age_prefer_bank(30,40)
        age_prefer_bank(40,50)
        age_prefer_bank(50,60)
        age_prefer_bank(60,0)
        
        age_repayment(0,20)
        age_repayment(20,30)
        age_repayment(30,40)
        age_repayment(40,50)
        age_repayment(50,60)
        age_repayment(60,0)
        
        age_prefer_loan(0,20)
        age_prefer_loan(20,30)
        age_prefer_loan(30,40)
        age_prefer_loan(40,50)
        age_prefer_loan(50,60)
        age_prefer_loan(60,0)
             
        #################  salary ########################
        
        salary_total(0,2)
        salary_total(2,3)
        salary_total(3,4)
        salary_total(4,5)
        salary_total(5,7)
        salary_total(7,10)
        salary_total(10,0)
        
        salary_prefer_loan(0,2)
        salary_prefer_loan(2,3)
        salary_prefer_loan(3,4)
        salary_prefer_loan(4,5)
        salary_prefer_loan(5,7)
        salary_prefer_loan(7,10)
        salary_prefer_loan(10,0) 
        
        ################ list #############################
        
        total_list()
        recent_list()
        age_list()
        
        #####################################
        print 'statistics end'
        threading.Timer(60,self.TaskA).start()

def main():
    init()
    print 'statistics thread init success'
    at = AsyncTask()
    at.TaskA()
    print 'statistics thread start'


if __name__ == '__main__':
    main()