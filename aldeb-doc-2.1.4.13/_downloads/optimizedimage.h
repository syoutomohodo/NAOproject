/**
 * @author
 *
 * This file was generated by Aldebaran Robotics ModuleGenerator
 */

#ifndef OPTIMIZEDIMAGE_OPTIMIZEDIMAGE_H
#define OPTIMIZEDIMAGE_OPTIMIZEDIMAGE_H

#include <boost/shared_ptr.hpp>
#include <alcommon/almodule.h>
#include <string>

#include <alproxies/alvideodeviceproxy.h>
#include <alvision/alimage.h>

namespace AL
{
  class ALBroker;
}

class OptimizedImage : public AL::ALModule
{
  public:

    OptimizedImage(boost::shared_ptr<AL::ALBroker> broker, const std::string& name);

    virtual ~OptimizedImage();

    void init();

    void optimizedImageProcessing();

  private:

    AL::ALVideoDeviceProxy fVideoProxy;
    std::string fGVMId;

    AL::ALImage* fImagePointer;

};

#endif  // OPTIMIZEDIMAGE_OPTIMIZEDIMAGE_H

