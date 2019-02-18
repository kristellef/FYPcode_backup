#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11.06.2013
@author: tessonec@ethz.ch
@version: 1.1.0 (29.08.13)
'''
#from sequential import SequentialAnaliser
from heuristics import SequenceCalculator
from utils import newline_msg

import os, os.path, time, datetime
import optparse

import networkx as nx
import numpy as np





class NetworkBuilder(SequenceCalculator):

    def __init__(self, options):


        SequenceCalculator.__init__(self,options)

        self.network_dir = "NET-%s-%s_%s"%(self.currency, self.heuristic, self.epoch)
#        self.file_out = open("NET-%s-%s.%s.info"%(self.currency, self.heuristic, self.epoch), "w")



        newline_msg("LOAD","identification")
        npz = np.load("%s/identification-%d_%d.npz" % (self.output_dir, options.load_period[0], options.load_period[1]))

        self.user_appeared = npz["arr_0"]
        self.no_uses = npz["arr_1"]
        newline_msg("LOAD","miner")

        self.miner_detected = np.load("%s/miner-%d_%d.npy" % (self.output_dir , options.load_period[0], options.load_period[1]) )


#        self.miner_detected = data["arr_0"]
#        self.mining_pool_detected = data["arr_1"]


        self.miners = self.miner_detected < self.max_blk
        self.sinks = self.no_uses == 1
        self.alltime_miners = self.miner_detected < self.max_blk
        self.miners = np.zeros( self.minimised_n_users, dtype = np.bool )

        self.net = nx.DiGraph()

        self.last_time = None
        self.current_time = None

        self.naddr_nstd = self.cfg['naddress_nonstandard']
        self.naddr_nspk = self.cfg['naddress_noscript-pk']
        self.naddr_ngen = self.cfg['naddress_generation']

        self.set_forbidden = set( [ self.naddr_nstd,  self.naddr_nspk, self.naddr_ngen] )





    def process(self, blk):

        
        self.current_time = self.get_time( blk )
        if self.last_time == None:
            self.last_time = self.current_time
            # try:
        all_transactions = blk.transactions
        # except :

        # ns: NON-SINK
        for (n_tx, ( transaction_hash, transaction_fee, transaction_size, transaction_input,transaction_output ) ) in enumerate( all_transactions  ):

            if len(transaction_input) == 0:
                  continue

            input_users = set()
            
            for ( user_in,qty ) in transaction_input:
                  input_users.add( user_in )
                  if user_in  == 0:
                      continue
                  

            is_generation = ( 0 in input_users )
            
            for input_user in input_users:

                if input_user in self.set_forbidden:
                    continue

                if is_generation:
                    input_is_miner = False
                    input_is_sink = False
                else:
                    input_is_miner = self.miners[ input_user ]
                    input_is_sink = self.sinks[ input_user ]

                    if not self.net.has_node( input_user ) and not is_generation:
                        self.net.add_node(input_user, is_miner = bool( input_is_miner ), is_sink = bool( input_is_sink) )
                    
                red_tx_output = {}

                for ( user_out,qty ) in transaction_output:
                    if user_out == input_user:
                        continue

                    if user_out in self.set_forbidden:
                        continue

                    if red_tx_output.has_key(user_out):
                        red_tx_output[user_out] += qty
                    else: 
                        red_tx_output[user_out] = qty
                
                for ( user_out,qty ) in red_tx_output.iteritems():
                    if is_generation:
                        self.miners[ user_out ] = True
                    output_is_miner = self.miners[ user_out ] 
                    output_is_sink = self.sinks[ user_out ]
      
                    if not self.net.has_node( user_out ):
                      self.net.add_node(user_out, is_miner = bool( output_is_miner ), is_sink = bool( output_is_sink) )
                    
                    if is_generation:
                        continue
                  
                    if self.net.has_edge(input_user, user_out):
                       edge = self.net[input_user][user_out] 
                       edge[ 'qty' ] += qty
                       edge[ 'no_transactions' ] += 1.
                    else:
                       self.net.add_edge(input_user, user_out, no_transactions = 1, qty = qty)







    def update_intermediate(self, **kwargs):

        msg_str = "processed block_id = %d [%s] ... nn = %d / ne = %d " % (
                                                  kwargs["block_id"],
                                                  time.strftime("%Y-%m-%d", time.gmtime(self.last_time)),
                                                  self.net.number_of_nodes(), self.net.number_of_edges() )
        newline_msg("MSG", msg_str )
        if self.file_log:
            newline_msg("MSG", msg_str, stream = self.file_log )
            self.file_log.flush()
       
        if self.last_time is None:
            return 
        

        if self.epoch == 'day':
            time_val = time.strftime("%Y-%m-%d", time.gmtime(self.last_time) )
        elif self.epoch == 'month':
            time_val = time.strftime("%Y-%m-01", time.gmtime(self.last_time) )
        elif self.epoch == "week":
            t_s = time.gmtime(self.last_time)
            dt = datetime.datetime(*t_s[:6])
            start = dt - datetime.timedelta(days=dt.weekday())
            time_val = start.strftime("%Y-%m-%d")
        elif self.epoch == "block":
            time_val = time.strftime("%Y-%m-%d", time.gmtime(self.last_time))

        else:
            time_val = self.last_time

        out_dir, key, fout_name = self.get_fname( **kwargs)
        if not os.path.exists(out_dir):
             os.makedirs(out_dir)

 #       print >> self.file_out, key, "%s/%s"%(out_dir, fout_name)
       # self.file_out.flush()
        nx.write_graphml(self.net, "%s/%s"%(out_dir, fout_name))

        self.net.clear()

        self.last_time = self.current_time

        
    def get_fname(self, **kwargs):
        block_id = kwargs['block_id']
        dir_name = self.network_dir

        if self.epoch == 'block':
            if self.save_each == 1:
                head = "block-%.6d"%(block_id)
                dir_name = "%s/%.3d"%(self.network_dir,block_id/1000 )
            else:
                head = "block-%.8d"%block_id
        elif self.epoch == 'day':
            head = time.strftime( "%Y-%m-%d" ,time.gmtime(self.last_time) )
        elif self.epoch == 'month':
            head = time.strftime( "%Y-%m" ,time.gmtime(self.last_time) )
        elif self.epoch == 'week':
            head = time.strftime( "%Y-%m-%d" ,time.gmtime(self.last_time) )
 
#        print self.epoch
        return  dir_name, head, head+".graphml"





       
        
#########################################################################################
#########################################################################################
def parse_command_line():
    parser = optparse.OptionParser()
    parser.add_option("--period",  action='store', dest="period",
                            default = "1,1" , help = "minimum block number to process" )

    parser.add_option("--load-period", action='store', dest="load_period",
                      default=None, help="minimum block number to process")

    parser.add_option("--save-each", type="int", action='store', dest="save_each",
                            default = 1 , help = "saves and updates status every SAVE_EACH" )

    parser.add_option("--epoch", action='store', dest="epoch",
                        default = None, help = "type of time-aggregation" )

    parser.add_option("--heur",action='store',dest='heuristic', default="1", help="run for given heuristics")

    parser.add_option("--curr", action='store', dest="currency", default = None,
                        help = "which currency is being analysed" )


    parser.add_option("--minimum-wealth", type="float", action='store', dest="minimum_wealth",
                            default = 1e-6 , help = "minimum wealth non trimmed" )



    options, args = parser.parse_args()

    options.heuristic = "heur_%s"%options.heuristic

    options.period = map( int, options.period.split(",") )
    assert len(options.period) == 2
    [options.min_blk , options.max_blk ]= options.period


    if options.load_period is not None:
        options.load_period = map(int, options.load_period.split(","))
    else:
        options.load_period = options.period


    options.log_filename = "LOG-net-0-%s-%d_%d.log" % (options.currency, options.min_blk, options.max_blk)


    return options, args
















if __name__ == "__main__":
      
      options, args = parse_command_line()
      proc = NetworkBuilder(options)

      newline_msg("PROC","running heuristics")
      proc.process_all()
      






