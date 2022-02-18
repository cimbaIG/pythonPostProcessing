#!/usr/bin/env python

from pylab import *

def load_pressure(filename):
    import os

    if not os.path.exists(filename):
        return None

    from numpy import zeros
    from vtk import vtkPolyDataReader, vtkCellDataToPointData

    reader = vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.Update()

    data = reader.GetOutput()

    # Extracting triangulation information
    triangles = data.GetPolys().GetData()
    points = data.GetPoints()

    # Mapping data: cell -> point
    mapper = vtkCellDataToPointData()
    mapper.AddInputData(data)
    mapper.Update()
    mapped_data = mapper.GetOutput()

    # Extracting interpolate point data
    udata = mapped_data.GetPointData().GetArray(0)

    ntri = triangles.GetNumberOfTuples()/4
    npts = points.GetNumberOfPoints()
    nvls = udata.GetNumberOfTuples()

    tri = zeros((ntri, 3))
    x = zeros(npts)
    y = zeros(npts)
    z = zeros(npts)
    pressure = zeros(nvls)
    Cp = zeros(nvls)

    for i in xrange(0, ntri):
        tri[i, 0] = triangles.GetTuple(4*i + 1)[0]
        tri[i, 1] = triangles.GetTuple(4*i + 2)[0]
        tri[i, 2] = triangles.GetTuple(4*i + 3)[0]

    for i in xrange(npts):
        pt = points.GetPoint(i)
        x[i] = pt[0]
        y[i] = pt[1]
        z[i] = pt[2]

    for i in xrange(0, nvls):
        p = udata.GetTuple(i)
        pressure[i] = p[0]
        Cp[i] = (pressure[i] - 8.61)/(0.5 * 1 * 14.92 * 14.92)

    return (x, y, z, tri, Cp)


def plot(filename):
    import os
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import clf, tricontour, tricontourf, \
        gca, savefig, rc, minorticks_on
    import matplotlib.patches as patches

    matplotlib.rcParams['mathtext.fontset'] = 'stix'
    matplotlib.rcParams['font.family'] = 'STIXGeneral'

    if not os.path.exists(filename):
        return -1

    #rc('text', usetex=True)
    #clf()
    x, y, z, tri, Cp = load_pressure(filename)
    #tricontourf(x, y, tri, ux, 32)
    #tricontour(x, y, tri, ux, 16, linestyles='-',
    #           colors='black', linewidths=0.25)
    #minorticks_on()
    #gca().set_aspect('equal')
    #gca().tick_params(direction='out', which='both')
    #gca().set_xticklabels([])
    #gca().set_yticklabels([])
    
    name, _ = os.path.splitext(filename)
    name = os.path.basename(name)

    #savefig('{0}.png'.format(name), dpi=300, bbox_inches='tight')
    #savefig('{0}.pdf'.format(name), bbox_inches='tight')

    # Mesh
    #plt.figure(figsize=(8, 8))
    #plt.triplot(x, y, tri)
    #plt.gca().set_aspect('equal')

    CpMin = np.min(Cp)
    CpMax = np.max(Cp)

    print "CpMin = ", CpMin
    print "CpMax = ", CpMax

    # Pressure
    fig = plt.figure('Pressure coefficient at top side', figsize=(10, 10))
    ax1 = fig.add_subplot(111, aspect='equal')
    ax1.add_patch(
        patches.Rectangle(
            (0.0, 0.0),   # (z,y)
            0.1,          # width
            0.2,          # height
            linewidth = 3,
    #        #hatch='x',
            fill=False
    #        #facecolor="#696969"
        )
    )
    v = np.linspace(-0.35, -0.15, 6, endpoint=True)
    xMin = 0.0
    xMax = 0.1
    yMin = 0.0
    yMax = 0.2
    matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
    CS = plt.tricontourf(z, y, tri, Cp,levels = v,extend = 'both', cmap='gist_yarg', alpha=0.7) #CS = plt.tricontourf(x, y, tri, ux, cmap=cm.coolwarm)
    cs = plt.tricontour(np.ma.masked_outside(z,xMin,xMax), np.ma.masked_outside(y,yMin,yMax), tri, Cp, v, linewidths = 1, colors = 'black') #plt.tricontour(x, y, tri, ux, cmap=cm.coolwarm)
    #manual_locations = [(0.025, 0.1), (0.075, 0.03), (0.075, 0.075)]
    #clabels = plt.clabel(cs, v, fmt='%4.1f', inline_spacing=-20)#, manual=manual_locations)
    #[txt.set_bbox(dict(facecolor='white', edgecolor='none', pad=0)) for txt in clabels]
    #cbar = plt.colorbar(CS, ticks=[pMin, pMax], orientation='horizontal')
    cbar = plt.colorbar(CS, ticks = v, orientation = 'horizontal', format='%.2f')
    #for label in cbar.ax.xaxis.get_ticklabels()[::2]:
    #    label.set_visible(False)
    print cbar
    #cbar.set_label(r'$C_\mathrm{p}$',size=30)
    cbar.ax.tick_params(labelsize=30) 
    plt.gca().set_aspect('equal')
    gca().tick_params(direction='out', which='both')
    gca().set_xticklabels([])
    gca().set_yticklabels([])
    plt.xlim([xMin, xMax])
    plt.ylim([yMin, yMax])
    plt.axis('off')    

    savefig('Cp_rearSide.png', dpi=900, bbox_inches='tight')
    savefig('Cp_rearSide.pdf', bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print 'usage: {0} [FILENAME]'.format(sys.argv[0])
        sys.exit(-1)
    sys.exit(plot(sys.argv[1]))
