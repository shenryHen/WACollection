package io.localhank.wac;

import java.util.AbstractMap;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class WACHashMap<K,V>
{
	private Map hashMap;

 	public WACHashMap(){
 		hashMap = new HashMap<K,V>();
 	}

 	public Object put(K key, V val){
 		return this.hashMap.put(key, val);
 	}

 	public Object get(K key){
 		return this.hashMap.get(key);
 	}

 	public Set<Map.Entry<K,V>> entrySet(){
 		return this.hashMap.entrySet();
 	}
}
