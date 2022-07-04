import React from "react";
import { ReactComponent as GithubIcon} from "../icons/github.svg";
import { ReactComponent as LinkedinIcon} from "../icons/linkedin.svg";
import IconSocial from "./IconSocial";

const SocialFlow = () => {
  return (
     <div className={"Social"}>
       <IconSocial icon={<GithubIcon className={"Icon"}/>} href={"https://github.com/djimontyp"}/>
       <IconSocial icon={<LinkedinIcon className={"Icon"}/>} href={"https://www.linkedin.com/in/maks-naumenko/"}/>


     </div>
  );
};

export default SocialFlow