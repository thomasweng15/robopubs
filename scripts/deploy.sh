eval "$(ssh-agent -s)"
cp google_compute_engine /home/travis/.ssh/google_compute_engine
cp google_compute_engine.pub /home/travis/.ssh/google_compute_engine.pub
chmod 600 /home/travis/.ssh/google_compute_engine
ssh-add /home/travis/.ssh/google_compute_engine
if [ ! -d "$HOME/google-cloud-sdk/bin" ]; then rm -rf $HOME/google-cloud-sdk; export CLOUDSDK_CORE_DISABLE_PROMPTS=1; curl https://sdk.cloud.google.com | bash; fi
source /home/travis/google-cloud-sdk/path.bash.inc
gcloud auth activate-service-account --key-file service_api_key.json
gcloud compute config-ssh
git remote add deploy thomas_weng11@instance-1.us-central1-f.api-project-371041928874:/home/thomas_weng11/robopubs.git
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
git push deploy HEAD:master