#!/bin/bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export CMSVER=CMSSW_11_2_0_pre10
export SCRAM_ARCH=slc7_amd64_gcc820
cmsrel $CMSVER
cd $CMSVER/src
# alias cmsenv='eval `scramv1 runtime -sh`'
cmsenv
git cms-init
git cms-merge-topic WilliamKorcari:HGCal_GAN_production
