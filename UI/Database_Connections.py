def get_data():
    import cx_Oracle
    from settings import DB_SERVICES
    con = cx_Oracle.connect(DB_Services["Username"]/DB_SERVICES["Password"@DB_SERVICES["HOST")
    print (con.version)
    cursor = con.cursor()
    sql="select * from sched_request where (status='New'and requestor is null) and rownum=1"
    number_of_rows = cursor.execute(sql);
    for r in number_of_rows:
        print(" -- ", r[0])
        return(r[0])
    print(number_of_rows)
    con.close()

def get_Account_From_Party(party_number):
    import cx_Oracle
    from settings import DB_SERVICES
    try:
        con = cx_Oracle.connect(DB_Services["Username"] / DB_SERVICES["Password" @ DB_SERVICES["HOST")
        print(con.version)
        cursor = con.cursor()
        str_partynumber = str(party_number)
        sql = "select Account_name from apps.hz_cust_accounts_all where party_id ='"+str_partynumber+"'"
        number_of_rows = cursor.execute(sql);
        for r in number_of_rows:
            print(" -- ", r[0])
            return (r[0])
    except:
        return("DNF")

def get_PartyID_From_Accountname(Account_Name):
    import cx_Oracle
    from settings import DB_SERVICES
    try:
        con = cx_Oracle.connect(DB_Services["Username"] / DB_SERVICES["Password" @ DB_SERVICES["HOST")
        print("Connected to Oracle Database Vesrion: ",con.version)
        cursor = con.cursor()
        str_partynumber = str(Account_Name)
        sql = "select party_id from apps.hz_cust_accounts_all where Account_name ='" + Account_Name + "'"
        number_of_rows = cursor.execute(sql);
        for r in number_of_rows:
            print(type( r[0]))
            if(type(r[0]) == None):
                return "DNF"
            else:
                return (r[0])
    except:
        return("DNF")

def get_CMF_Info(Account_Name):
        import cx_Oracle
        from settings import DB_SERVICES
    #try:
        con = cx_Oracle.connect(DB_Services["Username"] / DB_SERVICES["Password" @ DB_SERVICES["HOST")
        print("Connected to Oracle Database Vesrion: ", con.version)
        cursor = con.cursor()
        str_partynumber = str(Account_Name)
        sql = """SELECT HCA.ACCOUNT_NUMBER, HCA.ACCOUNT_NAME, HP.PARTY_NUMBER, HP.PARTY_NAME 
        FROM APPS.HZ_CUST_ACCOUNTS_ALL HCA, APPS.HZ_PARTIES HP  
        WHERE  HP.PARTY_ID =  HCA.PARTY_ID AND   
        HP.PARTY_NAME  =  '"""+Account_Name+"""'"""
        print(sql)
        cmf_info = cursor.execute(sql);
        print(cmf_info)
        cmf_list = []
        cmf_name_list = []
        res = ""
        i=0
        #print(len(cmf_info))
        for cmf in cmf_info:
            cmf_list.append(cmf[0])
            cmf_name_list.append(cmf[1])
            print(cmf[1])
        while i < len(cmf_name_list):
            res = res + cmf_name_list[i] + ',  '
            i = i + 1
        return res
    #except:
     #   return(["DNF"])



