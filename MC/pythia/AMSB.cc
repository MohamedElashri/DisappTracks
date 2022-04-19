#include "Pythia8/Pythia.h"

using namespace Pythia8;

int main() {
    // Generator. Shorthand for the event.
    Pythia pythia;
    Event& event = pythia.event;
    // Read in commands from external file.
    pythia.readFile("AMSB.cmnd");


    // Initialize.
    pythia.init();

// Histograms
    Hist decVtx("Chargino decay vertex (mm from origin)", 100, 0., 1000.);



    int nEvent   = pythia.mode("Main:numberOfEvents");
    int nAbort   = pythia.mode("Main:timesAllowErrors");
// Begin event loop.
    int iAbort = 0;
    for (int iEvent = 0; iEvent < nEvent; ++iEvent) {

        // Generate events. Quit if failure.
        if (!pythia.next()) {
            if (++iAbort < nAbort) continue;
            cout << " Event generation aborted prematurely, owing to error!\n";
            break;
        }

        // loop for chargino in the event
        for (int i = 0; i < event.size(); ++i) {
            int idAbs = event[i].idAbs();
            if (idAbs == 1000024) {
                // Separation of chargino decay vertex from the origin
                // double dist = event[i].vDec().pAbs(); // It give the same result
                double dist = sqrt(event[i].xDec() * event[i].xDec() +
                              event[i].yDec() * event[i].yDec() +
                              event[i].zDec() * event[i].zDec());
                decVtx.fill( dist);
                cout << "\n Chargino decay vertex (mm from origin)\n"<< dist << endl;

            }

        }

    }
    // Stats
    pythia.stat();

    // normalize histograms by 1/nEvent
    decVtx.normalizeSpectrum(nEvent);
    cout << decVtx << endl;
    //return 0;

    HistPlot hpl("DecayPlot");
    hpl.frame( "DecayVertex", "Chargino Decay Vertex (1000 GeV)", "Distance (mm)","Entries");
    hpl.add( decVtx, "h,red", "DecayVertex");
    hpl.plot();


    // Done
    return 0;

}