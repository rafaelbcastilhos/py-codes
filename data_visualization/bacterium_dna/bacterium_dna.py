# DNA mapping using fasta file
bac_in = open("bacterium.fasta").read()
bac_out = open("dna_table_out.html", "w")

count = {}

try:
    for i in ['A', 'T', 'C', 'G']:
        for j in ['A', 'T', 'C', 'G']:
            count[i + j] = 0

    bac_in = bac_in.replace("\n", "")

    for k in range(len(bac_in) - 1):
        count[bac_in[k] + bac_in[k + 1]] += 1

    i = 1
    for k in count:
        transparency = count[k] / max(count.values())
        bac_out.write(
            "<div style='width:100px; border:1px solid #111; color: #fff;height:100px; float:left; "
            "background-color:rgba(""0, 0, 0, " + str(transparency) + "')>" + k + "</div>")

        if i % 4 == 0:
            bac_out.write("<div style='clear:both'></div>")

        i += 1
except FileNotFoundError:
    print("file doesn't exist")

finally:
    bac_out.close()
