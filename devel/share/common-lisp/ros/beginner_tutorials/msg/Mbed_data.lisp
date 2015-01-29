; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude Mbed_data.msg.html

(cl:defclass <Mbed_data> (roslisp-msg-protocol:ros-message)
  ((time_stamp
    :reader time_stamp
    :initarg :time_stamp
    :type cl:string
    :initform "")
   (mbed_wheel_odometer
    :reader mbed_wheel_odometer
    :initarg :mbed_wheel_odometer
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0))
   (mbed_wheel_rotation
    :reader mbed_wheel_rotation
    :initarg :mbed_wheel_rotation
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Mbed_data (<Mbed_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mbed_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mbed_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<Mbed_data> is deprecated: use beginner_tutorials-msg:Mbed_data instead.")))

(cl:ensure-generic-function 'time_stamp-val :lambda-list '(m))
(cl:defmethod time_stamp-val ((m <Mbed_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:time_stamp-val is deprecated.  Use beginner_tutorials-msg:time_stamp instead.")
  (time_stamp m))

(cl:ensure-generic-function 'mbed_wheel_odometer-val :lambda-list '(m))
(cl:defmethod mbed_wheel_odometer-val ((m <Mbed_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:mbed_wheel_odometer-val is deprecated.  Use beginner_tutorials-msg:mbed_wheel_odometer instead.")
  (mbed_wheel_odometer m))

(cl:ensure-generic-function 'mbed_wheel_rotation-val :lambda-list '(m))
(cl:defmethod mbed_wheel_rotation-val ((m <Mbed_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:mbed_wheel_rotation-val is deprecated.  Use beginner_tutorials-msg:mbed_wheel_rotation instead.")
  (mbed_wheel_rotation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mbed_data>) ostream)
  "Serializes a message object of type '<Mbed_data>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'time_stamp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'time_stamp))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'mbed_wheel_odometer))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'mbed_wheel_rotation))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mbed_data>) istream)
  "Deserializes a message object of type '<Mbed_data>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time_stamp) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'time_stamp) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:setf (cl:slot-value msg 'mbed_wheel_odometer) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'mbed_wheel_odometer)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  (cl:setf (cl:slot-value msg 'mbed_wheel_rotation) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'mbed_wheel_rotation)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mbed_data>)))
  "Returns string type for a message object of type '<Mbed_data>"
  "beginner_tutorials/Mbed_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mbed_data)))
  "Returns string type for a message object of type 'Mbed_data"
  "beginner_tutorials/Mbed_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mbed_data>)))
  "Returns md5sum for a message object of type '<Mbed_data>"
  "7418c9c6fe4dfce9d9e0a65e1f6d6404")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mbed_data)))
  "Returns md5sum for a message object of type 'Mbed_data"
  "7418c9c6fe4dfce9d9e0a65e1f6d6404")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mbed_data>)))
  "Returns full string definition for message of type '<Mbed_data>"
  (cl:format cl:nil "string time_stamp~%float64[4] mbed_wheel_odometer~%float64[4] mbed_wheel_rotation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mbed_data)))
  "Returns full string definition for message of type 'Mbed_data"
  (cl:format cl:nil "string time_stamp~%float64[4] mbed_wheel_odometer~%float64[4] mbed_wheel_rotation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mbed_data>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'time_stamp))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'mbed_wheel_odometer) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'mbed_wheel_rotation) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mbed_data>))
  "Converts a ROS message object to a list"
  (cl:list 'Mbed_data
    (cl:cons ':time_stamp (time_stamp msg))
    (cl:cons ':mbed_wheel_odometer (mbed_wheel_odometer msg))
    (cl:cons ':mbed_wheel_rotation (mbed_wheel_rotation msg))
))
