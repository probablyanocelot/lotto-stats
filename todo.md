CREATE WRAPPER TO IGNORE PRINT STATEMENTS
        import sys, os

        # Disable
        def blockPrint():
            sys.stdout = open(os.devnull, 'w')

        # Restore
        def enablePrint():
            sys.stdout = sys.__stdout__


        print 'This will print'

        blockPrint()
        print "This won't"

        enablePrint()
        print "This will too"



1. REMOVE SHEETS FROM APP                               APP
2. APP BACK BUTTON                                      APP
3. MULTIPLE SPREADSHEET/LOTTERY FORMATS - current       BACKEND
4. PERSONAL PICKS                                       BOTH
5. APP CHARTS                                           BOTH
6. BUILD                                                V0.1



spin2win :
    enable sort by any col_name -- abstract & hide original purpose.
    enable csv/excel/JSON(?)

picks :
    iterate through winning numbers to check if matching





POWERBALL SHEET URL FOR TESTING=
    https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD&sorting=true