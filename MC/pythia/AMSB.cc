#include "Pythia8/Pythia.h"
#include <iostream>
#include "TVirtualPad.h"
#include "TApplication.h"
#include "TH1.h"         
#include <TH1F.h>   
#include "TFile.h"
#include <TCanvas.h>
#include <TF1Convolution.h>
#include <vector>
#include <iostream>

using namespace Pythia8;




int main() {
    // Generator. Shorthand for the event.
    Pythia pythia;
    Event& event = pythia.event;
    // Read in commands from external file.
    pythia.readFile("AMSB.cmnd");

    // To use with statistics
    int nEventAccepted[1] = { 0 };
    int nEventVetoed[2] = { 0, 0};
    const char *vetoStr[] = { "|eta|", "dist" };




    // Initialize.
    pythia.init();
    //pythia.particleData.listChanged();

    // Create file on which histogram(s) can be saved.
    TFile* outFile = new TFile("hist.root", "RECREATE");
    // Book histogram
    TH1F *decVtx = new TH1F("decVtx","Chargino decay vertex ", 100, 0, 10000);
    //TH1F *decVtx = new TH1F("decVtx","Chargino decay vertex ", 100, 900, 1000); // for the decay vertex in custom decay window
    // make exponential fit function
    int CHI = 1000024;
    cout << "Lifetime [mm] =" << scientific << pythia.particleData.tau0(CHI) << endl;
// Histograms
    //Hist decVtx("Chargino decay vertex (mm from origin)", 100., 0., 10000.);
    //Hist life("Decay lifetime (mm)" ,100,0,100.);



    int nEvent   = pythia.mode("Main:numberOfEvents");
    int nAbort   = pythia.mode("Main:timesAllowErrors");
// Begin event loop.
    int iAbort = 0;
    for (int iEvent = 0; iEvent < nEvent; ++iEvent) {
        if (!pythia.next()) continue;

        //life.fill(event[5].tau());
    
        // loop for chargino in the event
        for (int i = 0; i < event.size(); ++i) {
            int idAbs = event[i].idAbs();
            double eta = event[i].eta();
            if (idAbs == 1000024) {
                /*
                if (eta > 2  && eta < 5 ) {
                // Separation of chargino decay vertex from the origin
                // double dist = event[i].vDec().pAbs(); // It give the same result
                double dist = sqrt(event[i].xDec() * event[i].xDec() +
                              event[i].yDec() * event[i].yDec() +
                              event[i].zDec() * event[i].zDec());
                //decVtx.fill(dist);
                decVtx->Fill(dist);
                //cout << "\n Chargino decay vertex (mm from origin)\n"<< dist << endl;
                }
                */
                if (event[i].eta() > 2 && event[i].eta() < 5) {
                   nEventVetoed[0]++;
        
        

                   //double dist = event[i].vDec().pAbs();  
                   double dist = sqrt(event[i].xDec() * event[i].xDec() +
                              event[i].yDec() * event[i].yDec() +
                              event[i].zDec() * event[i].zDec());            
                   decVtx->Fill(dist);      
                   if (dist > 1000 && dist < 2000) {
                      nEventVetoed[1]++;
                      nEventAccepted[i]++;
                    }         
        }   
        }
        }

        

    }    
    // Stats
    pythia.stat();

    cout << endl << nEvent << " events generated. " << nEventAccepted[0]
    << " events passed cuts." << endl;
    
    // Show histogram. Possibility to close it.
    decVtx->Draw();
    //std::cout << "\nDouble click on the histogram window to quit.\n";
    //gPad->WaitPrimitive();
    // Save histogram on file and close file.
    decVtx->Write();
    delete outFile;

    // normalize histograms by 1/nEvent
    //decVtx.normalizeSpectrum(nEvent);
    //cout << decVtx << endl;
    //cout << life << endl;
    //return 0;

    //HistPlot hpl("DecayVertex");
    //hpl.frame( "DecayVertexPlot", "Chargino Decay (700 GeV)", "Distance/lifetime (mm)","Entries");
    //hpl.add( decVtx, "h,red", "DecayVertex");
    //hpl.plot();
    
    //HistPlot hpl("Decaylifetime");
    //hpl.frame( "DecaylifetimePlot", "Chargino Decay Vertex (1000 GeV)", "Life time (mm)","Entries");
    //hpl.add( life, "h,blue", "Decaylifetime");
    //hpl.plot();



    // Done
    return 0;

}
