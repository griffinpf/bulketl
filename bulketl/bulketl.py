class Directory:
    """
    Directory object describing where the files live and their type

    Args:
        filepath(str): The filepath of the directory containing the files
        filetype(str): The extension of the files to grab (.xlsx, .csv, etc).
    
    Attributes:
        files(list): List of files matching the filetype in the filepath (default [])
    """
    def __init__(self,filepath,filetype,files):
        self.filepath = filepath
        self.filetype = filetype
        self.files = []

    def getFiles(self):
        """
        Populates Directory.files with files that match specified criteria.
        """
        print("getFiles under development")
    

class Connection:
    """
    Connection to data warehouse

    Args:
        server(str): The name of the SQL Server to connect to
        table(str): The fully qualified (database.schema.table) table to write to
    """
    def __init__(self,server,table):
        self.server = server
        self.table = table

    def write(self,files,overwrite=False):
        """"
        Write the contents of files to data warehouse

        Args:
            files(Directory.files): The files to write
            overwrite(bool): Drop/recreate table (default False)
        """
        print("write under development")
