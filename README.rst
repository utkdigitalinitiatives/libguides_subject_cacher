================================
UT Libraries Libguides Cacher
================================

About
=====

This is used to cache the responses of LibGuides Subjects API requests to AWS so that we can limit the number of
Libguides requests we make each day.  It also stores cached copies of the response store in AWS in memory in Heroku.

Environmental Variables
=======================

All environmental variables (API keys, subject keys, time) are stored as config vars in Heroku.  You can generate the
response for a new subject by adding to the config var list and changing the time to a minute or two from now.  This
will force the jobber to generate new responses for everything.  Right now, we update each response daily.