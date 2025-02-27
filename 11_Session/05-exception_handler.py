def geh(is_tb = False , should_exit = False):
    from sys import exc_info 
    from traceback import print_tb

    exc_name, exc_data , exc_tb = exc_info()
    print(exc_name.__name__,exc_data,sep=":")

    if is_tb == True:
        from traceback import print_tb
        print_tb(exc_tb)
    if should_exit == True:
        sys.exit(-1)


 
