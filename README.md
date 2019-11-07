# BulkETL

BulkETL provides python functionality to load all Excel, CSV, or txt files in a given directory to a specified SQL Server backend


## Useage
  from bulketl import bulketl
  
  bulketl(filepath,filetype,server,table,overwrite)

## Arguments
- filepath(str): The filepath of the directory containing the files to load
- filetype(str): The extension of the files to grab (.xlsx,.csv,.txt)
- server(str): The name of the SQL Server to connect to
- table(str): The fully qualified (database.schema.table) table to write to
- overwrite(bool): Drop/recreate table (default False)
