
import config


from bruter_lib import *


def Main():
    """
    Multithread runner.
    """
    try:
        
        print('%s - Getting list of users ...' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
        usersList = GetListFromFile(config.usersFile)
        print('%s - Getting list of passwords ...' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
        passwordsList = [GetListFromFile(config.passwordsFile)]
        if len(passwordsList[0]) / config.brutThreads <= 1:
            config.brutThreads = 1
        if config.brutThreads > 1:
            print('%s - Separate passwords list by threads ...' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
            passwordsList = SeparateListByPieces(passwordsList[0], config.brutThreads)
        print('%s - Bruter initialize, status: oK' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))

       
        for i in range(config.brutThreads):
            OpenBrowser(i, config.timeout, config.selBrowserString, config.selFFProfile)
            GoingToTarget(i, config.timeout, config.target,
                          config.xPathLogin, config.xPathPassword, config.xPathAcceptButton)

            threads.append(threading.Thread(
                target=Bruter,
                args=(i, config.timeout, config.xPathLogin, config.xPathPassword, config.xPathAcceptButton,
                      config.xPathSuccessAuth, config.xPathFailAuth, usersList, passwordsList[i],
                      config.randomCredentials, config.resultFile)))

            et = EstimateTime(len(usersList), len(passwordsList[i]), config.timeout,
                              round(config.rumpUpPeriod / config.brutThreads))
            print('%s - Thread #%d, %s' % (datetime.now().strftime('%H:%M:%S %d.%m.%Y'), i, et))
            threads[i].start()

            if (config.brutThreads > 1) and (config.rumpUpPeriod > 0) and (i != config.brutThreads - 1):
                time.sleep(config.rumpUpPeriod / config.brutThreads)

      
        threadsAreInProgress = True
        while threadsAreInProgress:
            for t in threads:
                if t != None:
                    threadsAreInProgress = True
                    break
                else:
                    threadsAreInProgress = False

    except BaseException:
        print('%s - Bruter initialize, status: error' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
        traceback.print_exc()

    finally:
        status = Cleaner()
        sys.exit(status)



if __name__ == "__main__":
    arg = ParseArgs()
    if arg.generator != None:
        print('%s - Trying to generate a lot of random strings ...' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
        if GenerateFileWithRandomStrings(config.randomGeneratorParameter) == 0:
            print('%s - Generator, status: oK.' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
            sys.exit(0)
        else:
            print('%s - Generator, status: error.' % datetime.now().strftime('%H:%M:%S %d.%m.%Y'))
            sys.exit(1)
    Main()