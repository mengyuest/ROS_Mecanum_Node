
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "Mbed_data" :depends-on ("_package_Mbed_data"))
    (:file "_package_Mbed_data" :depends-on ("_package"))
  ))