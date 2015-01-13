django-as_eimp
==============

A Django app that serves as a coordinating and web server interface to a host of electric imp based services

ElectricImp is a service that combines a cloud based backend tightly
coupled with locally operating, wifi connected microcontrollers.
Their service handles a lot of the nasty complicated details of
getting your hardware online and connected to the network.

This django app serves as a web based entity that Electric Imp's will
register with and control interactions with them through this module.

So what does this app do:

1. A http endpoint where a new imp can register its existence
2. An admin UI where newly registered imps can be blessed/accepted
3. Upon blessing establish credentials and access keys such that
   through this django-app communications back to the eimp can be
   controlled.
4. An enumeration of the electric imps that are under your control.
5. A way to send messages to registered electric imps
6. A way to have callbacks invoked when messages from registered
   electric imps arrive.

We should have some basic DOS protection as well.. such as if we get
hundreds, thousands, millions of requests to register from network rogues.
