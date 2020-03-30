import os,sys
import ROOT as r
import h5py

def traverse_datasets(hdf_file):

    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            keystr=str(prefix+"/"+key)
            path = str(prefix+"/"+key) #f'{prefix}'
            if isinstance(item, h5py.Dataset): # test for dataset                                                                                                                                                         
                yield (path, item)
            elif isinstance(item, h5py.Group): # test for group (go down)                                                                                                                                                 
                yield from h5py_dataset_iterator(item, path)

    for path, _ in h5py_dataset_iterator(hdf_file):
        yield path


def draw2D(hist2d, xtitle, ytitle, ztitle, zmin, zmax, out, log):
    r.gROOT.SetBatch(True)
    can=r.TCanvas('can_'+str(hist2d.GetName()))
    if log:
        can.SetLogz()

    hist2d.GetXaxis().SetTitle(xtitle)
    hist2d.GetYaxis().SetTitle(ytitle)
    hist2d.GetZaxis().SetTitle(ztitle)
    hist2d.SetMaximum(zmax)
    hist2d.SetMinimum(zmin)
    hist2d.Draw("colz")
    
    can.Print(out)

def home():
    return os.getcwd()
