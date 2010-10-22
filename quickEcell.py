import ecell.Session as Session
import ecell.ecs
import ecell.config
import ecell.emc
import os
import sys
import matplotlib.pyplot as plt


class QuickEcell():

    def __init__(filename):
        """Initialize Ecell simulator creating a session and a simulator object
        and loading the model."""
        # set DM library   
        ecell.ecs.setDMSearchPath( os.pathsep.join( ecell.config.dm_path ) )
        # create sim obj
        self.sim = ecell.emc.Simulator()
        # create the session obj
        self.ses = Session.Session(sim, changeDirectory=False)
        # Lod the model
        try:
            ses.loadModel(filename)
        except IOError:
            print "File %s not found." %filename
        
        
    def create_loggers(variables):
        """Create the loggers. The variable name is the Key, the ecell logger obj 
        is the Value"""
        
        loggers = {}
        for var in variables:
            try:
                loggers[var] = ses.createLoggerStub('Variable:/:' + var + ':Value')
                loggers[var].create()
            except Error:
                print "The variable %s is not present in the model." %var
                print "Did you by chance mispelled?"
        return loggers

    def run_and_plot(time, variables):
        """Run the simulator and plot all the variables in the variables."""

        self.ses.run(time)        
        for var in variables:
            plotVar(var)
        plt.legend(loc=0)
        
    def plotVar(var):
        "Plot the specific variable"
        var_array = loggers[var].getData()
    #    print var_array
        plt.plot(var_array[:,0], var_array[:,1], label=var)
    
def demo():
    """Demo method. This should be the skeleton of your simulation"""
    
    qE = QuickEcell('simple_ecell_mod.eml')
    variables = ['S', 'P']
    loggers = qE.createLoggers(variables)
    qE.run_and_plot(1000, variables)

def demo_flux()
    """demo method to test the flux negative constant"""
    
    qE = QuickEcell('simple_ecell_mod.eml')
    variables = ['S', 'P']
    flux = qE.ses.createEntityStub('Process:/:C_S1')
    flux2 = qE.ses.createEntityStub('Process:/:C_S2')
    loggers = qE.createLoggers(variables)
    qE.ses.run(100)
    flux['k'] = -10
    flux['k'] = +4
    qE.run_and_plot(300)

if __name__ == '__main__' :
    print "Running the Demo"
    demo()

