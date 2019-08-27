# -*- coding: utf-8 -*-
#BEGIN_HEADER

from MetagenomeAPI.BinnedContigsIndexer import BinnedContigsIndexer
from Workspace.WorkspaceClient import Workspace
from MetagenomeAPI.AMAUtils import AMAUtils
#END_HEADER


class MetagenomeAPI:
    '''
    Module Name:
    MetagenomeAPI

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.1"
    GIT_URL = "https://github.com/slebras/MetagenomeAPI.git"
    GIT_COMMIT_HASH = "48b0191b78f137ddeb9fa6d8a58668c16c95491c"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.indexer = BinnedContigsIndexer(config)
        self.config = config
        #END_CONSTRUCTOR
        pass


    def search_binned_contigs(self, ctx, params):
        """
        :param params: instance of type "SearchBinnedContigsOptions"
           (num_found - optional field which when set informs that there is
           no need to perform full scan in order to count this value because
           it was already done before; please don't set this value with 0 or
           any guessed number if you didn't get right value previously.) ->
           structure: parameter "ref" of String, parameter "query" of String,
           parameter "sort_by" of list of type "column_sorting" -> tuple of
           size 2: parameter "column" of String, parameter "ascending" of
           type "boolean" (Indicates true or false values, false = 0, true =
           1 @range [0,1]), parameter "start" of Long, parameter "limit" of
           Long, parameter "num_found" of Long
        :returns: instance of type "SearchBinnedContigsResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "bins" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "bins" of list of
           type "ContigBinData" (bin_id          - id of the bin n_contigs   
           - number of contigs in this bin gc              - GC content over
           all the contigs sum_contig_len  - (bp) total length of the contigs
           cov             - coverage over the bin (if available, may be
           null)) -> structure: parameter "bin_id" of String, parameter
           "n_contigs" of Long, parameter "gc" of Double, parameter
           "sum_contig_len" of Long, parameter "cov" of Double, parameter
           "num_found" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_binned_contigs
        result = self.indexer.search_binned_contigs(ctx["token"],
                                                    params.get("ref", None),
                                                    params.get("query", None),
                                                    params.get("sort_by", None),
                                                    params.get("start", None),
                                                    params.get("limit", None),
                                                    params.get("num_found", None))
        #END search_binned_contigs

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_binned_contigs return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def search_contigs_in_bin(self, ctx, params):
        """
        :param params: instance of type "SearchContigsInBin" (num_found -
           optional field which when set informs that there is no need to
           perform full scan in order to count this value because it was
           already done before; please don't set this value with 0 or any
           guessed number if you didn't get right value previously.) ->
           structure: parameter "ref" of String, parameter "bin_id" of
           String, parameter "query" of String, parameter "sort_by" of list
           of type "column_sorting" -> tuple of size 2: parameter "column" of
           String, parameter "ascending" of type "boolean" (Indicates true or
           false values, false = 0, true = 1 @range [0,1]), parameter "start"
           of Long, parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchContigsInBinResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "bins" list).) -> structure: parameter "query" of
           String, parameter "bin_id" of String, parameter "start" of Long,
           parameter "contigs" of list of type "ContigInBin" (contig_id      
           - id of the contig len             - (bp) length of the contig gc 
           - GC content over the contig cov             - coverage over the
           contig (if available, may be null)) -> structure: parameter
           "contig_id" of String, parameter "len" of Long, parameter "gc" of
           Double, parameter "cov" of Double, parameter "num_found" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_contigs_in_bin
        result = self.indexer.search_contigs_in_bin(ctx["token"],
                                                    params.get("ref", None),
                                                    params.get("bin_id", None),
                                                    params.get("query", None),
                                                    params.get("sort_by", None),
                                                    params.get("start", None),
                                                    params.get("limit", None),
                                                    params.get("num_found", None))
        #END search_contigs_in_bin

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_contigs_in_bin return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_annotated_metagenome_assembly(self, ctx, params):
        """
        :param params: instance of type
           "getAnnotatedMetagenomeAssemblyParams" (ref - workspace reference
           to AnnotatedMetagenomeAssembly Object included_fields - The fields
           to include from the Object included_feature_fields -) ->
           structure: parameter "ref" of String, parameter "included_fields"
           of list of String
        :returns: instance of type "getAnnotatedMetagenomeAssemblyOutput" ->
           structure: parameter "genomes" of list of unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_annotated_metagenome_assembly
        ws = Workspace(self.config['workspace-url'], token=ctx['token'])
        ama_utils = AMAUtils(ws)
        output = ama_utils.get_annotated_metagenome_assembly(params)
        #END get_annotated_metagenome_assembly

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method get_annotated_metagenome_assembly return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
