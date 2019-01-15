import filecmp

from pkg_resources import resource_filename

from sargasso.separator.data_types import get_data_type_manager
from sargasso.separator.separators import *


def test_separator_manager_return_correct_separator_instance():
    assert isinstance(get_data_type_manager(['rnaseq'], Separator.DOC).get_separator(), RnaSeqSeparator)
    assert isinstance(get_data_type_manager(['dnaseq'], Separator.DOC).get_separator(), DnaSeqSeparator)


def test_run_rnaseq_pe_makefile(tmpdir):
    args = ["rnaseq",
            "--reads-base-dir={}".format(resource_filename("tests.data", "raw_reads")),
            "--num-threads", "2", "--best",
            "--sambamba-sort-tmp-dir", "/tmp",
            resource_filename('tests.data.pe.rnaseq', 'rnaseq.tsv'),
            tmpdir.join("rnaseq_test_pe").strpath,
            "mouse", "/srv/data/genome/mouse/ensembl-94/STAR_indices/primary_assembly",
            "human", "/srv/data/genome/human/ensembl-94/STAR_indices/primary_assembly",
            "rat", "/srv/data/genome/rat/ensembl-94/STAR_indices/toplevel"
            ]
    get_data_type_manager(['rnaseq'], Separator.DOC).get_separator().run(args)

    assert filecmp.cmp(resource_filename('tests.data.pe.rnaseq', 'Makefile'),
                       tmpdir.join("rnaseq_test_pe/Makefile").strpath), "Something wrong with rnaseq make file!"
    # assert filecmp.cmp(resource_filename('tests.data.rnaseq', 'execution_record.txt'),
    #                    tmpdir.join(
    #                        "rnaseq_test/execution_record.txt").strpath), "Something wrong with excution record file!"


def test_run_chipseq_se_makefile(tmpdir):
    args = ["dnaseq",
            "--reads-base-dir={}".format(resource_filename("tests.data", "raw_reads")),
            "--num-threads", "2", "--best",
            "--sambamba-sort-tmp-dir", "/tmp",
            resource_filename('tests.data.se.chipseq', 'chipseq.tsv'),
            tmpdir.join("chipseq_test_se").strpath,
            "mouse", "/srv/data/genome/mouse/ensembl-94/bowtie2_indices/primary_assembly",
            "human", "/srv/data/genome/human/ensembl-94/bowtie2_indices/primary_assembly",
            "rat", "/srv/data/genome/rat/ensembl-94/bowtie2_indices/toplevel"
            ]
    get_data_type_manager(['dnaseq'], Separator.DOC).get_separator().run(args)

    assert filecmp.cmp(resource_filename('tests.data.se.chipseq', 'Makefile'),
                       tmpdir.join("chipseq_test_se/Makefile").strpath), "Something wrong with chipseq make file!"



def test_run_chipseq_pe_makefile(tmpdir):
    args = ["dnaseq",
            "--reads-base-dir={}".format(resource_filename("tests.data", "raw_reads")),
            "--num-threads", "2", "--best",
            "--sambamba-sort-tmp-dir", "/tmp",
            resource_filename('tests.data.pe.chipseq', 'chipseq.tsv'),
            tmpdir.join("chipseq_test_pe").strpath,
            "mouse", "/srv/data/genome/mouse/ensembl-94/bowtie2_indices/primary_assembly",
            "human", "/srv/data/genome/human/ensembl-94/bowtie2_indices/primary_assembly",
            "rat", "/srv/data/genome/rat/ensembl-94/bowtie2_indices/toplevel"
            ]
    get_data_type_manager(['dnaseq'], Separator.DOC).get_separator().run(args)
    assert filecmp.cmp(resource_filename('tests.data.pe.chipseq', 'Makefile'),
                       tmpdir.join("chipseq_test_pe/Makefile").strpath), "Something wrong with chipseq make file!"