#auteur = Larsse Vink

import sqlconnection

def retrieve(uuid):

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()

    # username and password are match, update database
    # create storage date
    storagedate = ""

    userInfo = sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})
    # Controleer of de fiets al gestald is of niet
    if userInfo[3] != 0:
        dataobject = { "storagestate" : "0", "storagedate" : storagedate }
        sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})
        print('U kunt uw fiets ophalen.')
    else:
        print('Uw fiets staat nog niet in de stalling.')