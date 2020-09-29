/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package io.adaptivecards.objectmodel;

public class DateTimePreparsedToken {
  private transient long swigCPtr;
  private transient boolean swigCMemOwn;

  protected DateTimePreparsedToken(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(DateTimePreparsedToken obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void swigSetCMemOwn(boolean own) {
    swigCMemOwn = own;
  }

  @SuppressWarnings("deprecation")
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        AdaptiveCardObjectModelJNI.delete_DateTimePreparsedToken(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public DateTimePreparsedToken() {
    this(AdaptiveCardObjectModelJNI.new_DateTimePreparsedToken__SWIG_0(), true);
  }

  public DateTimePreparsedToken(String text, DateTimePreparsedTokenFormat format) {
    this(AdaptiveCardObjectModelJNI.new_DateTimePreparsedToken__SWIG_1(text, format.swigValue()), true);
  }

  public DateTimePreparsedToken(String text, CTime date, DateTimePreparsedTokenFormat format) {
    this(AdaptiveCardObjectModelJNI.new_DateTimePreparsedToken__SWIG_2(text, CTime.getCPtr(date), date, format.swigValue()), true);
  }

  public String GetText() {
    return AdaptiveCardObjectModelJNI.DateTimePreparsedToken_GetText(swigCPtr, this);
  }

  public DateTimePreparsedTokenFormat GetFormat() {
    return DateTimePreparsedTokenFormat.swigToEnum(AdaptiveCardObjectModelJNI.DateTimePreparsedToken_GetFormat(swigCPtr, this));
  }

  public int GetDay() {
    return AdaptiveCardObjectModelJNI.DateTimePreparsedToken_GetDay(swigCPtr, this);
  }

  public int GetMonth() {
    return AdaptiveCardObjectModelJNI.DateTimePreparsedToken_GetMonth(swigCPtr, this);
  }

  public int GetYear() {
    return AdaptiveCardObjectModelJNI.DateTimePreparsedToken_GetYear(swigCPtr, this);
  }

}
