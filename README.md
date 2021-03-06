# ThorlabsKinesis-KCubePiezo

A python module wrapping the native C inertial motor DLL manufactured
by ThorLabs Inc and using Kinesis API. This code was tested on
the ThorLabs product 
[KIM101](https://www.thorlabs.com/thorproduct.cfm?partnumber=KIM101),
a four-channel K-Cube Piezo Inertia Motor
Controller.

## Quick Start
Clone and install the repository using:

    >>> git clone https://github.com/yvesauad/ThorlabsKinesis-KCubePiezo.git
    >>> python setup.py install

Test simply using your motor serial number, which can be found
in the product closure, and typing:

    >>> from Modules import Kinesis_PMC
    >>> my_piezo = Kinesis_PMC.TLKinesisPiezoMotorController('97101411')
    >>> my_piezo.MoveAbsolute(1, 0)

This will move your first channel piezo to the absolute
0 position. A more complete example can be found in
`RunningTest.py`

## Problems and Improvements
The DLL is not entirely wrapped. It is possible that
some features are not available. Please fell free to
contribute to this repository or to contact us.
Sorry for adding the DOC (>32 MB). It took me few days
to find these and this could be your case as well.