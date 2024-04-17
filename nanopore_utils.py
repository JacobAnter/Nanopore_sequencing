import numpy as np

seq_file_path = "001c577a-a502-43ef-926a-b883f94d157b.true_fasta"
raw_sig_file_path = "001c577a-a502-43ef-926a-b883f94d157b.raw_signal"

def bundle_seq_and_sig(seq_path, sig_path):
    """
    This function accepts as input the paths to two files, the first of
    which harbours sequence information and the second of which harbours
    the Nanopore raw signals. Subsequently, both the sequence and the
    raw signal information are extracted in order to bundle them into a
    NumPy array.

    Parameters
    ----------
    seq_path: str
        Path to the file harbouring the sequence information. This file
        must adhere to the FASTA format, i.e. one entry consists of two
        individual lines, the first of which contains the so-called
        header and the second of which contains the actual sequence. It
        is assumed that one file comprises only one entry, i.e. two
        lines in total.
    sig_path: str
        Path to the file harbouring the Nanopore raw signals. Each value
        is expected to occupy a separate line.

    Returns
    -------
    bundled_array: NumPy array, dtype=, shape=(n,)
        ...
    """

    with open(seq_path) as f:
        _, seq = f.readlines()

    with open(sig_path) as f:
        # The individual elements in the list returned by readlines()
        # are strings; hence, they need to be converted into integers
        # Conveniently enough, the built-in int() function inherently
        # ignores the newline command, making special handling obsolete
        raw_sig_list = [int(line) for line in f.readlines()]
    
    combined_seq_and_sig = [seq] + raw_sig_list

    bundled_array = np.array(combined_seq_and_sig)

    return bundled_array

print(bundle_seq_and_sig(seq_file_path, raw_sig_file_path))