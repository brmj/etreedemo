import xml.etree.cElementTree as ET
 
#----------------------------------------------------------------------
def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    #print (tree.getroot())
    root = tree.getroot()
    #print ("tag=%s, attrib=%s" % (root.tag, root.attrib))

    problem = root.find("problem")[0]
    algorithm = root.find("algorithm")[0]
    #Could maybe do things a bit nicer using a schema if etree can work with that?

    if problem.tag == "classification_problem":
        clss = problem.findall("classes")
        if (len(clss) == 0):
            classes = 2
        else:
            classes = clss[0].text
        print ("This is a classification problem with ", classes, " classes.")

            
    else:
        print("This is some other problem, like prediction or something.")
    filename = problem.find("filename").text

    print ("data file location: ", filename)

    
    if algorithm.tag == "rf_classifier":
        trs = algorithm.findall("trees")
        if (len(trs) == 0):
            trees = 30 #An arbitrary default.
        else:
            trees = trs[0].text
        dpth = algorithm.findall("max_depth")
        if (len(dpth) == 0):
            depth = -1 #for unlimited.
        else:
            depth = dpth[0].text
        print ("We will solve it with a random forest classifier with ", trees, " trees and a max depth of ", depth, ".")
        #the stuff to actually do it (or at least convert to an internal implementation) goes here.
    else:
        print ("This is some other algorithm, maybe a neural network or an SVM or something.")


if __name__ == "__main__":
    parseXML("xmldemo.xml")
