import sys
import os
import subprocess
from time import sleep


def is_video_file(filename):
    """
        Detect only video files, not srts or other
    """
    # Source :
    # http://stackoverflow.com/questions/14919609/is-this-file-a-video-python
    video_file_extensions = (
        '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2',
        '.60d', '.787', '.89', '.aaf', '.aec', '.aep', '.aepx', '.aet', '.aetx',
        '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt',
        '.arcut', '.arf', '.asf', '.asx', '.avb', '.avc', '.avd', '.avi',
        '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2',
        '.bdt3', '.bik', '.bin', '.bix', '.bmk', '.bnp', '.box', '.bs4', '.bsf',
        '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine',
        '.cip', '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi',
        '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat', '.dav', '.dce', '.dck',
        '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb',
        '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss', '.dmx', '.dnc', '.dpa',
        '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr',
        '.dvr-ms', '.dvx', '.dxr', '.dzm', '.dzp', '.dzt', '.edl', '.evo',
        '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp',
        '.fcproject', '.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp',
        '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264', '.hdmov',
        '.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf',
        '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs', '.izz',
        '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec',
        '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21', '.m21', '.m2a', '.m2p',
        '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani',
        '.meta', '.mgv', '.mj2', '.mjp', '.mjpg', '.mk3d', '.mkv', '.mmv',
        '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov',
        '.movie', '.mp21', '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg',
        '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl',
        '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh',
        '.mswmm', '.mts', '.mtv', '.mvb', '.mvc', '.mvd', '.mve', '.mvex',
        '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut',
        '.nuv', '.nvc', '.ogm', '.ogv', '.ogx', '.osp', '.otrkey', '.pac',
        '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist',
        '.plproj', '.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj',
        '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr', '.pxv', '.qt',
        '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd',
        '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd', '.rmp', '.rms',
        '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts', '.rum', '.rv',
        '.rvid', '.rvl', '.sbk', '.sbt', '.scc', '.scm', '.scm', '.scn',
        '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv',
        '.smi', '.smi', '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz',
        '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi', '.swt',
        '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0',
        '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt', '.tvs', '.usf',
        '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx',
        '.veg', '.vem', '.vep', '.vf', '.vft', '.vfw', '.vfz', '.vgz',
        '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3',
        '.vp6', '.vp7', '.vpj', '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp',
        '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot',
        '.wp3', '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl',
        '.xlmv', '.xmv', '.xvid', '.y4m', '.yog', '.yuv', '.zeg', '.zm1',
        '.zm2', '.zm3', '.zmv')

    if filename.endswith((video_file_extensions)):
        return True
    return False


def getLength(filename):
    """
        Wibbly-wobbly documenty-wocumenty .stuff
    """
    # Source
    # :http://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python/3844467#3844467
    result = subprocess.Popen(["ffprobe", filename],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return [x.decode("utf-8") for x in result.stdout.readlines() if b"Duration" in x]


def get_time(filename):
    """
        Get time of each video in hh:mm:ss format
    """
    # print(getLength(loc))    # ['  Duration: 00:46:21.06, start: 0.000000,
    # bitrate: 1054 kb/s\n']
    details = getLength(filename)[0].split(',')
    # print(details[0]) #   Duration: 00:46:21.06
    d = details[0].split(': ')
    return d[1]


def run_time(path, outstr, binge):
    """
        Find run time of all videofiles.
    """
    sleep(1)
    print(path)
    outstr += path+"\n"
    episodes = os.listdir(path)
    videos = list()        # lazy approach because not all were listed
    for filer in episodes:
        # print(filer,is_video_file(filer))
        if is_video_file(filer):
            videos.append(filer)

    for episode in videos:
        time = get_time(path+'/'+episode)
        if time == "N/A":
            videos.remove(episode)
            continue
        t = time.split(':')
        binge[2] += int(float(t[2]))
        binge[1] += int(t[1]) + int(binge[2]/60)
        binge[2] %= 60
        binge[0] += int(t[0]) + int(binge[1]/60)
        binge[1] %= 60

        print( "\t", episode, "\t", time, "\t\t", binge[0], ":", binge[1], ":", binge[2])
        outstr += "\t"+episode+"\t"+time+"\t\t" + \
            str(binge[0])+":"+str(binge[1])+":"+str(binge[2])+"\n"

    print ("\nTime to complete this season : ", binge[0], ":", binge[1], ":", binge[2])
    outstr += "\nTime to complete this season : " + \
        str(binge[0])+":"+str(binge[1])+":"+str(binge[2])+"\n"

    return outstr


def main():
    """
        Get shit done.
    """
    # os.system('clear')

    # outfile= open('info.txt', 'a')
    outstr = ""
    path = input(
        "\n\nEnter the complete path of the directory whose length you want to know: ")

    seasons = os.listdir(path)
    # print (seasons)

    total = [None]*3
    total[0] = 0  # hours
    total[1] = 0  # minutes
    total[2] = 0  # seconds

    for each in seasons:
        if not os.path.isdir(path+'/'+each):  # if not directory
            continue
        binge = [None]*3
        binge[0] = 0  # hours
        binge[1] = 0  # minutes
        binge[2] = 0  # seconds
        outstr = run_time(path+'/'+each, outstr, binge)

        total[2] += int(binge[2])
        total[1] += binge[1] + int(total[2]/60)
        total[2] %= 60
        total[0] += binge[0] + int(total[1]/60)
        total[1] %= 60
        print ("\nTotal time elapsed : ", total[0], ":", total[1], ":", total[2])
        print ("\n\n")
        outstr += "\nTotal time elapsed : " + \
            str(total[0])+":"+str(total[1])+":"+str(total[2])+"\n\n\n"

    # make a report
    print ("Report saved at "+path)
    outfile = open(path+'/binge-timer.txt', 'w')
    outfile.write(outstr)
    outfile.close()


if __name__ == '__main__':
    main()
