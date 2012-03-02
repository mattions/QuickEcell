from mySession import Session
import ecell.ecs
import ecell.config
import ecell.emc
import os
import sys
import matplotlib.pyplot as plt


class QuickEcell():

    def __init__(self, filename):
        """Initialize Ecell simulator creating a session and a simulator object
        and loading the model."""
        # set DM library   
        ecell.ecs.setDMSearchPath( os.pathsep.join( ecell.config.dm_path ) )
        # create sim obj
        self.sim = ecell.emc.Simulator()
        # create the session obj
        self.ses = Session(self.sim, changeDirectory=False)
        # Lod the model
        try:
            self.ses.loadModel(filename)
        except IOError:
            print "IOError: File %s not found." %filename
        
        
    def create_loggers(self, variables):
        """Create the loggers. The variable name is the Key, the ecell logger obj 
        is the Value"""
        
        loggers = {}
        for var in variables:
        	try:
        		loggers[var] = self.ses.createLoggerStub('Variable:/:' + var + ':Value')
	        	loggers[var].create()
	        except RuntimeError:
	        	print "Variable %s not in the model" %var
	        	print "You need to use the same name you've used in the em file."
	        
        return loggers

    def run_and_plot(self, time, variables, loggers):
        """Run the simulator and plot all the variables in the variables."""

        self.ses.run(time)        
        for var in variables:
            self.plot_var(var, loggers)
        plt.legend(loc=0)
        
    def plot_var(self, var, loggers):
        "Plot the specific variable"
        try:
        	var_array = loggers[var].getData()
    		plt.plot(var_array[:,0], var_array[:,1], label=var)
    	except RuntimeError:
    		print "Var %s not in the loggers. Skipping" %var
    
def demo():
    """Demo method. This should be the skeleton of your simulation"""
    
    qE = QuickEcell(os.path.join('models', 'simple_ecell_mod.eml'))
    variables = ['S', 'P']
    loggers = qE.create_loggers(variables)
    qE.run_and_plot(1000, variables, loggers)
    plt.title("Test for Michaelis-Menten")
    plt.show()

def demo_flux():
    """demo method to test the flux negative constant"""
    
    qE = QuickEcell(os.path.join('models', 'constant_flux.eml'))
    variables = ['S1', 'S2']
    flux = qE.ses.createEntityStub('Process:/:C_S1')
    flux2 = qE.ses.createEntityStub('Process:/:C_S2')
    loggers = qE.create_loggers(variables)
    qE.ses.run(100)
    flux['k'] = -10
    flux2['k'] = +4
    qE.run_and_plot(300, variables, loggers)
    plt.title('Test fo Constant Flux')
    plt.show()

if __name__ == '__main__' :
    print "Running the Demos"
    print 
    demo()
    plt.figure()
    demo_flux()

