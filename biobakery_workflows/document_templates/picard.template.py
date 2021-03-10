
#+ echo=False
# if picard files are provided, then plot those that do not meet a threshold
picard_text = ""

picard_min_threshold=20
# read through all picard files, capturing those based on the threshold
data_below_threshold={}
samples_above_threshold=[]

for file in utilities.get_files(vars["picard"], extension=vars["picard_ext"]):
    picard_sample_name = os.path.basename(file).replace("."+vars["picard_ext"],"")
    picard_data, below_threshold = utilities.read_picard(file, threshold=picard_min_threshold)
    if picard_data:
        if below_threshold:
            data_below_threshold[picard_sample_name]=[a[1] for a in picard_data]
        else:
            samples_above_threshold.append(picard_sample_name)

# plot each sample that is below the threshold
for sample, picard_data in data_below_threshold.items():
    document.plot_barchart(picard_data,
        title="Picard quality scores for "+sample, xlabel="Cycle", ylabel="Quality Score")
   
if len(data_below_threshold.keys()) > 0:
    picard_text="Only the samples with at least one quality score below the threshold "+\
        " ( "+str(picard_min_threshold)+" ) are shown as quality scores for each base. These samples are: "+\
        ",".join(list(data_below_threshold.keys()))+"."
else:
    picard_text="All samples had all quality scores above the threshold "+\
        " ( "+str(picard_min_threshold)+" )."
   
# list those that were above the threshold
above_threshold_list=",".join(samples_above_threshold)
if above_threshold_list:
    picard_text+=" The following samples did not have any quality scores below the threshold: " + above_threshold_list + "."
else:
    picard_text+=" None of the samples had all quality scores above the threshold."

#' <% if picard_text: print(picard_text) %>

