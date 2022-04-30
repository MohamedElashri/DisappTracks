# /usr/bin/env python3

'''
This Script is used to fit a histogram with an exponential function.
ß
Usage: python3 exp_fit.py -bin_number <bin_number> -input_file <root_file> -hist_name <histogram_name> -output_file <output_file_name> --low <low_range>

Author: Mohamed Elashri
Date:   2022-05-01

'''

from ROOT import TFile, TH1F, TF1, TCanvas, gROOT, TStyle, TPaveLabel
import ROOT

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--bin_number", dest="rebin_number",help="Number of bins in the histogram (for re-bin)", default=10)
parser.add_option("-i", "--input_file", dest="input_file",help="Input ROOT file")
parser.add_option("-n", "--hist_name", dest="hist_name",help="Name of the histogram")
parser.add_option("-o", "--output_file", dest="output_file",help="Output ROOT file")
parser.add_option("-l", "--low_range", dest="low_fit",help="Lower limit of fit range")
parser.add_option("-u", "--high_range", dest="high_fit",help="Upper limit of fit range")
parser.add_option("--nobatch", action="store_true", dest="nobatch",help="Do not run in batch mode")
(arguments, args) = parser.parse_args()


# Prevent canvas pop-up
if not arguments.nobatch:
    gROOT.SetBatch(True)
else:
    gROOT.SetBatch(False)    

inputfile=TFile(arguments.input_file, "READ")
hist = inputfile.Get(arguments.hist_name).Clone()
if not hist:
    print ("No TH1 Found" + arguments.hist_name + "in" + inputfile)

if arguments.rebin_number:
    hist.Rebin(int(arguments.rebin_number)) 

ROOT.gStyle.SetOptStat(111111)
ROOT.gStyle.SetOptFit(1111)
low_fit = hist.GetBinLowEdge(1)
high_fit = hist.GetBinLowEdge(hist.GetNbinsX()+1)   #+1 because it starts from 0
if arguments.low_fit:
    low_fit = float(arguments.low_fit)
if arguments.high_fit:
    high_fit = float(arguments.high_fit)
print ("low_fit =" + str(low_fit))
print ("high_fit =" + str(high_fit))    
exp_func = TF1("exp_func", "expo", low_fit, high_fit)
canvas = TCanvas()
hist.Fit("exp_func", "R") #R is for range
hist.Draw("pe")
#canvas.SetLogy(1)

print ("Fit fuction: exp([0]+[1]*x) in range (" + str(low_fit) + "," + str(high_fit) + ")")         #[0] is the constant, [1] is the slope
print ("The fit parameters are: [0] = " + str(exp_func.GetParameter(0)) + " [1] = " + str(exp_func.GetParameter(1)))

tau = -1.0 / exp_func.GetParameter(1)
tau_high_err = (-1.0 / exp_func.GetParameter(1) + exp_func.GetParError(1)) - tau
tau_low_err = (-1.0 / exp_func.GetParameter(1) - exp_func.GetParError(1)) - tau

print ("The fit parameters are: tau = -1./[1] = " + str(tau) + " +/- " + str(tau_high_err) + " - " + str(tau_low_err))

histname = arguments.hist_name
histname = histname[histname.rfind('/')+1:] #remove trailing slash
out_root = arguments.input_file.replace(".root", "_" + histname + "_exp_fit.root")
output_file= TFile(out_root, "RECREATE")

FitT= "The fitted <tau> = " + str.format("{0:.2f}", tau) + " +/- " + str.format("{0:.2f}", tau_high_err) + " - " + str.format("{0:.2f}", tau_low_err) + "}"

Fit_label = TPaveLabel(0.2, 0.8, 0.6, 0.9, FitT, "brNDC")
Fit_label.SetFillColor(0)
Fit_label.SetBorderSize(0)
Fit_label.SetFillStyle(0)
Fit_label.Draw()


# Now write the histogram to the output file
hist.Write()
canvas.Write()
output_file.Close()
output_filePDF = out_root.replace(".root", ".pdf")
canvas.SaveAs(output_filePDF)

print ("The plot is saved in " + output_filePDF + "and" + out_root)
print ("The script is done")
