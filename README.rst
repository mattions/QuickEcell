******************
Quick Ecell README
******************

This is a file that shows out to to use ecell in an `ipython` session with the 
`pylab` integration.

The classical skeleton is found in the demo class::

    # Load the model and create the objs
    qE = QuickEcell('simple_ecell_mod.eml') 
    
    # Create the variables. 
    # the name has to match the one you've used in the model
    variables = ['S', 'P']
    
    # Create the loggers to have the data
    loggers = qE.createLoggers(variables)
    
    # Run and plot it.
    qE.run_and_plot(1000, variables, loggers)
    

Basically copy and paste that as your main script, or create a main method which
resembles this one.

There is also a `demo_flux` which actually test the Constant Flux. Maybe can be of some use to someone.

If the module is launched as main it just run the two demos.

*******
License
*******

Under GPL3 http://www.gnu.org/licenses/gpl-3.0.html

Have fun,
Michele Mattioni.
