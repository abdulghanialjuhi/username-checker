import httpRequest from '../tools/httpRequest';
import { FiTwitter, FiInstagram } from 'react-icons/fi'
import { RiSnapchatLine } from 'react-icons/ri'
import { FaTiktok, FaGoogle, FaReddit } from 'react-icons/fa'
import { SiMicrosoftoutlook } from 'react-icons/si'
import { useState } from 'react';

export default function useGlobal() {

    const [platforms, setPlatForms] = useState([
        {
            name: 'Instagram',
            logo: <FiInstagram size={30} />,
            status: null,
            reason: null,
            url: '/check/instagram',
            restrictions: ['_.', 30]
        },
        {
            name: 'Twitter',
            logo: <FiTwitter size={30} />,
            status: null,
            reason: null,
            url: '/check/twitter',
            restrictions: ['_', 14, 5]

        },
        {
            name: 'Snapchat',
            logo: <RiSnapchatLine size={30} />,
            status: null,
            reason: null,
            url: '/check/snapchat',
            restrictions: ['_.-', 15, 3]
        },
        {
            name: 'Tiktok',
            logo: <FaTiktok size={30} />,
            status: null,
            reason: null,
            url: '/check/tiktok',
            restrictions: ['_.', 24, 2]
        },
        {
            name: 'Gmail',
            logo: <FaGoogle size={30} />,
            status: null,
            reason: null,
            url: '/check/gmail',
            restrictions: ['.', 30, 6]
        },   
        {
            name: 'Hotmail',
            logo: <SiMicrosoftoutlook size={30} />,
            status: null,
            reason: null,
            url: '/check/hotmail',
            restrictions: ['_.-', 64]
        },
        {
            name: 'Outlook',
            logo: <SiMicrosoftoutlook size={30} />,
            status: null,
            reason: null,
            url: '/check/outlook',
            restrictions: ['_.-', 64]
        },
        {
            name: 'Reddit',
            logo: <FaReddit size={30} />,
            status: null,
            reason: null,
            url: '/check/reddit',
            restrictions: ['_-', 21, 4]
        },
    ])

    const checkUserNames = (username) => {

        platforms.forEach(((platforms) => {
            platforms.status = null
            platforms.reason = null
        }))

       

        platforms.forEach((platform, i) => {
            let fd = new FormData()
            fd.append('username', username)

            fd.append('restrictions', platform.restrictions)

            httpRequest.post(platform.url, fd)
            .then((res) => {
                let nreArr = [...platforms]
                nreArr[i].status = res.data.status
                nreArr[i].reason = res.data.reason
                setPlatForms(nreArr)
                
            })
            .catch((err) => {
                console.log(err)
            })
        })
        
    }

    function smoothScroll(target1) {
        const duration = 1500
        const target = document.querySelector(target1);
        const targetPosition = target.getBoundingClientRect().top;
        const startPosition = window.pageYOffset;
        const distance = targetPosition;
        let startTime = null;
  
        function animation(currentTime){
            if (startTime === null ) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = easeLinear(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        }

        function easeLinear (t, b, c, d) {
            return c * ((t = t / d - 1) * t * t + 1) + b;
        }

        requestAnimationFrame(animation);
    }



  return { smoothScroll, checkUserNames, platforms }
}
